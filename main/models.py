# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
    # Добавляем дополнительные поля.
    about = models.TextField(verbose_name="Обо мне", blank=True, null=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    phone1 = models.IntegerField(verbose_name='Телефон №1', blank=True, null=True)
    phone2 = models.IntegerField(verbose_name='Телефон №2', blank=True, null=True)
    mysite = models.URLField(verbose_name='Сайт', blank=True, null=True)
    vk = models.URLField(verbose_name='Вконтакте', blank=True, null=True)
    fb = models.URLField(verbose_name='FaceBook', blank=True, null=True)
    

