from django.db import models

# Create your models here.


class Land_Details(models.Model):
    land_address = models.TextField(max_length=500)
    previous_owner = models.CharField(max_length=250)
    current_owner = models.CharField(max_length=250)
    secret_password = models.CharField(default="none", max_length=300)
    land_id = models.CharField(max_length=100)
    date_sale = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
