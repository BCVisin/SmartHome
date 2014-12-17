from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('SmartHome.garage.views',
	url(r'trigger/$', 'garage_door_trigger', name='garage_door_trigger'),
	url(r'status/$', 'garage_door_status', name='garage_door_status'),

)
