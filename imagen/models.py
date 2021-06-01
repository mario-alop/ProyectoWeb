from django.db import models
from django.contrib.auth.models import User
from django_thumbs.fields import ImageThumbsField
from django.utils.html import format_html

# Create your models here.

class Image_thumbs(models.Model):
    
    SIZES = (
        {'code': 'avatar', 'wxh': '125x125', 'resize': 'crop'},
        {'code': 'm', 'wxh': '640x480', 'resize': 'scale'},
        {'code': 'flatrow', 'wxh': 'x120'},
        {'code': '150', 'wxh': '150x150'}, # 'resize' defaults to 'scale'
        )
    
    STATUS_CHOICES = (          #definimos los estados
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
    )
    
    id = models.AutoField(null=False, primary_key=True, unique=True)
    image = ImageThumbsField(upload_to='imagen_thumbs', verbose_name='Imagen', sizes=SIZES)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='inactiva')

    def get_image(self):
        if self.image:
            return format_html('<img src="{}"/>'.format(self.image.url_avatar))
        else:
            return '(Sin imagen)'
    get_image.short_description = 'miniatura'
    
    class Meta:
        ordering = ('id',)
    def __str__(self) -> str:
        return self.nombre