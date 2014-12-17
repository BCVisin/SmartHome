from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render_to_response
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.conf import settings
from SmartHome import utils

import json


@login_required
def home(request):

	context = {'PROJECT_NAME': settings.PROJECT_NAME, 'PROJECT_TITLE': settings.PROJECT_TITLE}

	sense_events = utils.sense_events()
	context['garage_door_open'] = str(sense_events.sense_garage_open()).lower()

	return render_to_response('home.html', context, context_instance=RequestContext(request))


def user_login(request):

	logout(request)

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		print user
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('home'))

	context = {'PROJECT_NAME': settings.PROJECT_NAME, 'PROJECT_TITLE': settings.PROJECT_TITLE}

	return render_to_response('login.html', context, context_instance=RequestContext(request))
