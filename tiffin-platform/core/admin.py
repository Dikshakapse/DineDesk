from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tiffin, Order

admin.site.register(Tiffin)
admin.site.register(Order)

