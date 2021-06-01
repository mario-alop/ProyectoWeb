from django.db import models
from django.shortcuts import render
from .models import Album, Image

# Create your views here.

def galeria(request):
    imagen = Image.objects.filter(estado='activa')
    return render(request, 'galeria/galeria.html',
                    {'imagen':imagen})

def album(request, album_id):
    album = Album.objects.get(id=album_id)
    imagen = Image.objects.filter(id=album)
    return render(request,'galeria/album.html',{'album':album},{'imagen':imagen})