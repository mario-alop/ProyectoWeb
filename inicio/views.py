from django.shortcuts import render
#from .models import Inicio

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')
