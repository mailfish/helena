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
            field=models.ImageField(help_text='Размер изображения 200px на 200px', upload_to='static/images', verbose_name='Изображение альбома'),
            preserve_default=True,
        ),
    ]
