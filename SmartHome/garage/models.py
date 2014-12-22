from django.db import models
from django.contrib.auth.models import User


class garage(models.Model):

	class Meta:
		permissions = (
			("view", "view"),
			("trigger", "trigger"),
		)


class garage_log(models.Model):

	GARAGE_ACTIONS = (
									(1, 'trigger'),
									(2, 'get_status'),
									)

	GARAGE_RESULTS = (
									(1, 'open'),
									(2, 'closed'),
									(3, 'unknown')
									)

	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	action = models.IntegerField(choices=GARAGE_ACTIONS)
	result = models.IntegerField(choices=GARAGE_RESULTS, null=True)
