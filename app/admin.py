from django.contrib import admin
from django.contrib import admin
from .models import (Land_Details)

# Register your models here.


@admin.register(Land_Details)
class Land_DetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'land_address', 'previous_owner', 'current_owner']
