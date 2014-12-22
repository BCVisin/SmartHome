from django.db import models
from SmartHome import gpio_pins
from django.contrib.auth.models import User

class lights(models.Model):

	class Meta:
		permissions = (
			("view", "view"),
			("trigger", "trigger"),
		)

class lights_log(models.Model):

	LIGHT_ACTIONS = (
										(1, 'on'),
										(2, 'off'),
										(3, 'get_status'),
									)
	LIGHT_RESULTS = (
										(1, 'on'),
										(2, 'off'),
										(3, 'unknown'),
									)

	LIGHT_IDS = (
								(gpio_pins.CHRISTMAS_LIGHTS_ZONE_ONE, 'CHRISTMAS_LIGHTS_ZONE_ONE'),
								(gpio_pins.GARAGE_LIGHTS_ZONE_ONE, 'GARAGE_LIGHTS_ZONE_ONE'),
								(gpio_pins.GARAGE_LIGHTS_ZONE_TWO, 'GARAGE_LIGHTS_ZONE_TWO'),
							)

	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	light_id = models.IntegerField(choices=LIGHT_IDS)
	action = models.IntegerField(choices=LIGHT_ACTIONS)
	result = models.IntegerField(choices=LIGHT_RESULTS, null=True)
