from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.galeria, name='galeria'),
    path('album/<int:album_id>', views.album, name='album')
]