from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
from django.http import FileResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import LandDetailsForm, LandBuyerForm
from .models import Land_Details
from django.db.models import Q
import hashlib

A = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@']


def home(request):
    return render(request, 'buysell.html')


class Sell_land(View):
    def get(self, request):
        form = LandDetailsForm()
        return render(request, 'seller.html', {'form': form})

    def post(self, request):
        form = LandDetailsForm(request.POST)
        if form.is_valid():
            land_address = form.cleaned_data['land_address']
            current_owner = form.cleaned_data['current_owner']
            land_id = form.cleaned_data['land_id']
            secret_password = form.cleaned_data['secret_password']

            land_exists = Land_Details.objects.filter(
                land_address=land_address, current_owner=current_owner, land_id=land_id).exists()

            if(land_exists == True):
                exist_info = Land_Details.objects.get(Q(land_address=land_address) & Q(
                    current_owner=current_owner) & Q(land_id=land_id))
                secret = exist_info.secret_password

                newsecret_password = hashlib.sha512(secret_password.encode())
                newsecret_password = str(newsecret_password.hexdigest())
                if(newsecret_password == secret):
                    temp_value = land_address + "||" + current_owner + "||" + land_id
                    temp_value = hashlib.sha512(temp_value.encode())
                    temp_value = str(temp_value.hexdigest())

                    send_id = temp_value
                    send_id += '||||||'

                    for i in land_id:
                        for j in range(0, len(A)):
                            if(i == A[j]):
                                send_id += A[len(A)-1-j]

                    send_id += '||||||'

                    for i in secret_password:
                        for j in range(0, len(A)):
                            if(i == A[j]):
                                send_id += A[len(A)-1-j]

                    print(send_id)

                    return render(request, 'copyable.html', {'data': send_id})
                else:
                    return render(request, 'incorrectdetails.html')

            else:
                return render(request, 'incorrectdetails.html')


class Buy_land(View):
    def get(self, request):
        form = LandBuyerForm()
        return render(request, 'buyer.html', {'form': form})

    def post(self, request):
        form = LandBuyerForm(request.POST)
        if form.is_valid():
            land_address = form.cleaned_data['land_address']
            current_owner = form.cleaned_data['current_owner']
            sender_det = form.cleaned_data['sender_det']

            x = sender_det.split("||||||")

            land_id = x[1]
            password_of = x[2]

            hash_of = x[0]

            land_idtemp = ""
            for i in land_id:
                for j in range(0, len(A)):
                    if(i == A[j]):
                        land_idtemp += A[len(A)-1-j]

            password_oftemp = ""
            for i in password_of:
                for j in range(0, len(A)):
                    if(i == A[j]):
                        password_oftemp += A[len(A)-1-j]

            print(land_idtemp)
            print(password_oftemp)
            print(hash_of)

            land_exists = Land_Details.objects.filter(
                land_address=land_address, current_owner=current_owner, land_id=land_idtemp).exists()

            if(land_exists == True):

                exist_info = Land_Details.objects.get(Q(land_address=land_address) & Q(
                    current_owner=current_owner) & Q(land_id=land_idtemp))
                secret = exist_info.secret_password

                newsecret_password = hashlib.sha512(password_oftemp.encode())
                newsecret_password = str(newsecret_password.hexdigest())

                if(secret == newsecret_password):
                    temp_value = land_address + "||" + current_owner + "||" + land_idtemp
                    temp_value = hashlib.sha512(temp_value.encode())
                    temp_value = str(temp_value.hexdigest())

                    if(temp_value == hash_of):
                        new_buyer = form.cleaned_data['buyer']
                        new_buy_pass = form.cleaned_data['buyer_password']

                        exist_info.previous_owner = current_owner
                        exist_info.current_owner = new_buyer

                        new_buy_pass = hashlib.sha512(new_buy_pass.encode())
                        new_buy_pass = str(new_buy_pass.hexdigest())

                        exist_info.secret_password = new_buy_pass
                        exist_info.save()

                        buf = io.BytesIO()
                        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
                        textob = c.beginText()
                        textob.setTextOrigin(inch, inch)
                        textob.setFont("Helvetica", 14)
                        lines = []

                        exist_info = Land_Details.objects.get(
                            Q(land_address=land_address))
                        lines.append(exist_info.land_address)
                        lines.append(exist_info.previous_owner)
                        lines.append(exist_info.current_owner)

                        textob.textLine("Registration Document")
                        textob.textLine("                     ")
                        textob.textLine("Land Address sold:  ")
                        textob.textLine("Sold by: " + lines[1])
                        textob.textLine("Sold To: " + lines[2])

                        c.drawText(textob)
                        c.showPage()
                        c.save()
                        buf.seek(0)

                        return FileResponse(buf, as_attachment=True, filename='document.pdf')
                    else:
                        return render(request, 'incorrectdetails.html')
                else:
                    return render(request, 'incorrectdetails.html')
            else:
                return render(request, 'incorrectdetails.html')
