from django.shortcuts import render
from .models import Empresa

# Create your views here.

def empresa_list(request):
    empresa = Empresa.objects.filter(estado='publicado')
    return render(request, 'empresa/empresa.html',{'empresa': empresa})