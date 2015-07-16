# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20150617_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('about', models.TextField(verbose_name='Обо мне', null=True, blank=True)),
                ('address', models.CharField(verbose_name='Адрес', max_length=300, null=True, blank=True)),
                ('phone1', models.IntegerField(verbose_name='Телефон-1', max_length=30, null=True, blank=True)),
                ('phone2', models.IntegerField(verbose_name='Телефон-2', max_length=30, null=True, blank=True)),
                ('skype', models.CharField(verbose_name='Skype', max_length=30, null=True, blank=True)),
                ('vk', models.URLField(verbose_name='Вконтакте', max_length=100, null=True, blank=True)),
                ('fb', models.URLField(verbose_name='FaceBook', max_length=100, null=True, blank=True)),
                ('site', models.URLField(verbose_name='Сайт в интернете', max_length=100, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
