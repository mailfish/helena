#! coding: utf-8
from django.db import models
from sorl.thumbnail import ImageField
from sorl.thumbnail.shortcuts import get_thumbnail
# Create your models here.
##Альбомы с фотографиями
class Album(models.Model):
    title = models.CharField("Название альбома", max_length=100)
    slug = models.SlugField("Ссылка на альбом", max_length=100, unique=True)
    img = ImageField("Изображение альбома", upload_to='static/images', help_text="Размер изображения 200px на 200px")


    def get_thumbnail_html(self):
        img = self.img
        img_resize_url = get_thumbnail(img, '100x100').url
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.img.url, img_resize_url, self.title)
    get_thumbnail_html.short_description = u'Миниатюра'
    # get_thumbnail_html.allow_tags = True

    class Meta:
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
    def __str__(self):
        return self.title

##Фотографии в альбоме

class Photo(models.Model):
    title = models.CharField("Название фотографии", max_length=100)
    album = models.ForeignKey(Album, verbose_name='Альбом')
    img = ImageField("Фото", upload_to='static/images', help_text="Фотографии с разрешением более 2048 × 2048 пикселей")

    def get_thumbnail_html(self):
        img = self.img
        img_resize_url = get_thumbnail(img, '100x100').url
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.img.url, img_resize_url, self.title)
    get_thumbnail_html.short_description = u'Миниатюра'
    get_thumbnail_html.allow_tags = True

    class Meta:
        ordering = ['title']
        verbose_name='Фото'
        verbose_name_plural='Фотографии'
    def __str__(self):
            return self.title