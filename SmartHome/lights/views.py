from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from SmartHome import utils

import json
import time


@user_passes_test(lambda u: u.has_perm('lights.trigger'))
def lights_trigger(request):

	pin = request.GET.get('pin')
	action = request.GET.get('action')

	trigger_events = utils.trigger_events(user=request.user)

	rtn = trigger_events.toggle_light(pin=int(pin), state=int(action))

	context = {'light_success': rtn}

	return HttpResponse(json.dumps(context))


@user_passes_test(lambda u: u.has_perm('lights.view'))
def lights_status(request):

	pin = request.GET.get('pin')

	sense_events = utils.sense_events(user=request.user)

	context = {'light_status': sense_events.sense_light(pin=int(pin))}

	return HttpResponse(json.dumps(context))
