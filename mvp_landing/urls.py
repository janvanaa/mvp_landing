from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^admin/', include(admin.site.urls)),
    )

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
