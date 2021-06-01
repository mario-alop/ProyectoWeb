from django.shortcuts import render
from django.http import HttpResponse
from .models import Anuncio
import datetime
# Create your views here.


def anuncio_list(request):
    anuncios = Anuncio.objects.filter(estado='publicado')
    return render(request, 'anuncios/anuncios.html',
                {'anuncios': anuncios})