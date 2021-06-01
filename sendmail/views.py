from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
        try:
            send_mail(nombre, subject, message, from_email,
            ['mario.alop@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')
    return render(request, 'sendmail/email.html', {'form': form})

def successView(request):
    return HttpResponse('Enviado! Gracias por el mensaje.')