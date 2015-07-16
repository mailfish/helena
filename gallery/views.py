from django.shortcuts import render
from gallery.models import Album, Photo
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.


class PhotoListView(DetailView):
    model = Album
    context_object_name = 'photos'
    template_name = 'photo.html'
