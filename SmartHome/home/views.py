from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from SmartHome import utils

def home(request):

	trigger_events = utils.trigger_events()

	if request.GET.get('trigger'):
		trigger_events.toggle_garage_door()

	context = {'PROJECT_NAME': settings.PROJECT_NAME, 'PROJECT_TITLE': settings.PROJECT_TITLE}

	return render_to_response('home.html', context, context_instance=RequestContext(request))




