from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.

class Album(models.Model):
    nombre = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('nombre',)
        verbose_name = 'album'
        verbose_name_plural = 'albums'
    def __str__(self):
        return self.nombre

class Image(models.Model):
    STATUS_CHOICES = (          #definimos los estados
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
    )
    owner = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Albun')
    id = models.AutoField(null=False, primary_key=True, unique=True)
    image = models.ImageField(upload_to='galeria', verbose_name='image')
    nombre = models.CharField(max_length=100)
    #albums = models.ManyToManyField(Album)
    estado = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='inactiva')

    def get_image(self):
        if self.image:
            return format_html('<img src="{}" style="width: 120px; \
                        height: 100px"/>'.format(self.image.url))
        else:
            return '(Sin imagen)'
    
    get_image.short_description = 'miniatura'

    
    class Meta:
        ordering = ('id',)
        verbose_name = 'image'
        verbose_name_plural = 'images'
    def __str__(self) -> str:
        return self.nombre
    
