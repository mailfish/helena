# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='img',
            field=models.ImageField(upload_to='static/images', verbose_name='Изображение альбома', help_text='Размер изображения 200px на 200px'),
            preserve_default=True,
        ),
    ]
