from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Empresa(models.Model):
    STATUS_CHOICES = (          #definimos los estados
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=50, verbose_name='Título')
    contenido = RichTextField(verbose_name='Contenido')
    autor = models.CharField(max_length=150, null=False, verbose_name='Autor')
    imagen = models.ImageField(null = True, upload_to='images', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Última Edición')
    estado = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='borrador')
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ('-created',)
        
    def __str__(self):
        return self.titulo