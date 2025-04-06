from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Tiffin

def home(request):
    tiffins = Tiffin.objects.all()
    return render(request, 'core/home.html', {'tiffins': tiffins})
