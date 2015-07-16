from django.conf.urls import patterns, url
from .views import PhotoListView


urlpatterns = patterns('',
                       url(r'^(?P<slug>[\w-]+)/$', PhotoListView.as_view(), name='image'),
)