#coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from gallery.models import Album

# Create your views here.

def index(request):
    return render_to_response('index.html',
    {'my_album':Album.objects.all()})
