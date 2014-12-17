from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from SmartHome.garage import urls as garage_urls
from django.views.generic.simple import direct_to_template

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

context = {'PROJECT_NAME': settings.PROJECT_NAME, 'PROJECT_TITLE': settings.PROJECT_TITLE}

urlpatterns = patterns('',

		url(r'^$', 'SmartHome.home.views.home', name='home'),
		(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
		(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

		url(r'^garage/', include(garage_urls)),
		(r'^manifest.json$', direct_to_template, {'extra_context': context, 'template': 'manifest.html', 'mimetype':'application/json'}),

		url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
		url(r'^admin/', include(admin.site.urls)),
)
