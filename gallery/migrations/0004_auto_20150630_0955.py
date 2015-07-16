# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150611_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='img',
            field=sorl.thumbnail.fields.ImageField(upload_to='static/images', help_text='Размер изображения 200px на 200px', verbose_name='Изображение альбома'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=sorl.thumbnail.fields.ImageField(upload_to='static/images', help_text='Фотографии с разрешением более 2048 × 2048 пикселей', verbose_name='Фото'),
            preserve_default=True,
        ),
    ]
