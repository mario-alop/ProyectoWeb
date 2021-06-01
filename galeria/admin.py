from django.contrib import admin
from .models import Album, Image
from django.utils.html import format_html


# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','image','get_image']

admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)