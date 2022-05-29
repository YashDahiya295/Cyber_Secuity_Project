from django.forms import ModelForm
from .models import Land_Details
from django import forms


class LandDetailsForm(ModelForm):
    class Meta:
        model = Land_Details
        fields = ['land_address', 'current_owner',
                  'land_id', 'secret_password']
        labels = {'land_address': 'Enter the address of the land ',
                  'current_owner': 'Enter the current owner name ',
                  'land_id': 'Enter the ID of the land ',
                  'secret_password': 'Enter the password '}
        widgets = {'land_address': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}),
                   'current_owner': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}),
                   'land_id': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}),
                   'secret_password': forms.PasswordInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'})}


class LandBuyerForm(ModelForm):

    sender_det = forms.CharField(
        label='Sender Inputs ', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}))
    buyer = forms.CharField(
        label='Buyer Name ', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}))
    buyer_password = forms.CharField(
        label='Buyer Password ', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}))

    class Meta:
        model = Land_Details
        fields = ['land_address', 'current_owner', 'sender_det']
        labels = {'land_address': 'Enter the address of the land ',
                  'current_owner': 'Enter the current owner name '}
        widgets = {'land_address': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'}),
                   'current_owner': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-family: Asap,sans-serif'})}
