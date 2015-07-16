#coding:utf-8
from django.contrib import admin
from gallery.models import Photo, Album
# Register your models here.

#
#Для Альбома
class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title','slug','img']})
    ]
    list_display = ['get_thumbnail_html', 'title']
    list_display_links = ['title', ]
    prepopulated_fields = {'slug': ['title']}
    ordering = ['title']

#
#Для рисунка
class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title','album','img']})
    ]
    list_display = ['get_thumbnail_html', 'title']
    list_display_links = ['title', ]
    ordering = ['title']

#
#Регистрируем
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)