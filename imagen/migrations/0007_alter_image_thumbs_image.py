# Generated by Django 3.2 on 2021-05-15 16:48

from django.db import migrations
import django_thumbs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imagen', '0006_alter_image_thumbs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_thumbs',
            name='image',
            field=django_thumbs.fields.ImageThumbsField(sizes=({'code': 'avatar', 'resize': 'crop', 'wxh': '125x125'}, {'code': 'm', 'resize': 'scale', 'wxh': '640x480'}, {'code': 'flatrow', 'wxh': 'x120'}, {'code': '150', 'wxh': '150x150'}), upload_to='imagen_thumbs'),
        ),
    ]
