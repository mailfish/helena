from django.conf.urls import patterns, include, url
from django.contrib import admin
#####this is for devel-op only###
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helena.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('main.urls')),
    #url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^gallery/', include('gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
