from django.core.management.base import BaseCommand, CommandError

from SmartHome import utils
from SmartHome import gpio_pins

import time

class Command(BaseCommand):
	help = 'Run this to constantly check to see if we should toggle the garage lights if the door is open or closed'

	def handle(self, *args, **options):

		sense_events = utils.sense_events(log_event=False)
		trigger_events = utils.trigger_events(log_event=False)

		last_state = 'OFF'

		while True:

			if sense_events.sense_garage_open() == 'false':
				if last_state == 'ON':
					trigger_events.toggle_light(pin=gpio_pins.GARAGE_LIGHTS_ZONE_ONE, state=2)
					last_state = 'OFF'
					self.stdout.write('Garage is closed so we are turning lights off\n')
			else:
				if last_state == 'OFF':
					trigger_events.toggle_light(pin=gpio_pins.GARAGE_LIGHTS_ZONE_ONE, state=1)
					last_state = 'ON'
					self.stdout.write('Garage is open(ing) so we are turning lights on\n')

			time.sleep(1)
