from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from SmartHome import utils

import json
import time


@user_passes_test(lambda u: u.has_perm('garage.trigger'))
def garage_door_trigger(request):

	trigger_events = utils.trigger_events()

	trigger_events.toggle_garage_door()

	sense_events = utils.sense_events()

	time.sleep(10)

	context = {'garage_door_open':sense_events.sense_garage_open()}

	return HttpResponse(json.dumps(context))


@user_passes_test(lambda u: u.has_perm('garage.view'))
def garage_door_status(request):

	sense_events = utils.sense_events()

	context = {'garage_door_open':sense_events.sense_garage_open()}

	return HttpResponse(json.dumps(context))
