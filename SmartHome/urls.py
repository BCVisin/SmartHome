from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'SmartHome.home.views.home', name='home'),
    url(r'^accounts/login/$', 'SmartHome.home.views.login'),

    url(r'^garage/$', include('SmartHome.garage.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
