from django.shortcuts import render
from .models import  Image_thumbs

# Create your views here.

def imagen(request):
    respuesta = Image_thumbs.objects.filter(estado='activa')
    return render(request, 'imagen/imagen.html',
                    {'imagen':respuesta})