# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название альбома', max_length=100)),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на альбом', max_length=100)),
                ('img', models.ImageField(help_text='Размер изображения 200px на 200px', verbose_name='Изображение альбома', upload_to='img')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Альбомы',
                'verbose_name': 'Альбом',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название фотографии', max_length=100)),
                ('img', models.ImageField(help_text='Фотографии с разрешением более 2048 × 2048 пикселей', verbose_name='Фото', upload_to='img')),
                ('album', models.ForeignKey(to='gallery.Album', verbose_name='Альбом')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Фотографии',
                'verbose_name': 'Фото',
            },
            bases=(models.Model,),
        ),
    ]
