from django.contrib import admin
from .models import  Image_thumbs

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','image','get_image']

admin.site.register(Image_thumbs, ImageAdmin)
