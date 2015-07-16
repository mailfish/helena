# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150611_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='static/images', verbose_name='Фото', help_text='Фотографии с разрешением более 2048 × 2048 пикселей'),
            preserve_default=True,
        ),
    ]
