from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from SmartHome import utils

import json


@user_passes_test(lambda u: u.has_perm('garage.trigger'), login_url='/?error=Your user does not have the required permissions to access the requested page.')
def garage_door_trigger(request):

	trigger_events = utils.trigger_events()

	trigger_events.toggle_garage_door()

	error = request.GET.get('error') or None

	context = {'error': error}

	return HttpResponse(json.dumps(context))
