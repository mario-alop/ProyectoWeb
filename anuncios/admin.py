from django.contrib import admin
from .models import Anuncio

# Register your models here.

class AnunciosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#admin.site.register(Anuncio)

admin.site.register(Anuncio, AnunciosAdmin)
