from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
from SmartHome import utils

import json


@login_required
def home(request):

	context = {'PROJECT_NAME': settings.PROJECT_NAME, 'PROJECT_TITLE': settings.PROJECT_TITLE}

	return render_to_response('home.html', context, context_instance=RequestContext(request))


def login(request):

	context = {'PROJECT_NAME': settings.PROJECT_NAME, 'PROJECT_TITLE': settings.PROJECT_TITLE}

	return render_to_response('login.html', context, context_instance=RequestContext(request))
