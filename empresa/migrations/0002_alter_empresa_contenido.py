# Generated by Django 3.2 on 2021-05-04 18:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
