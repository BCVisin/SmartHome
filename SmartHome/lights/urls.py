from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('SmartHome.lights.views',
	url(r'trigger/$', 'lights_trigger', name='lights_trigger'),
	url(r'status/$', 'lights_status', name='lights_status'),

)
