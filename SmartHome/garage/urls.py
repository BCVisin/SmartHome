from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('garage.views',
	url(r'trigger/$', 'garage_door_trigger', name='garage_door_trigger'),
)
