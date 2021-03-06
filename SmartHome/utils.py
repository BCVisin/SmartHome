import gpio_pins
import time
import random

from SmartHome.lights.models import lights_log
from SmartHome.garage.models import garage_log


class trigger_events():

	def __init__(self, user=None, log_event=True):

		self.user = user
		self.log_event = log_event

		try:
			import RPi.GPIO as GPIO
			self.gpio_enabled = True
		except (RuntimeError, ImportError, NameError):
			self.gpio_enabled = False

	def toggle_garage_door(self):

		if self.gpio_enabled:
			import RPi.GPIO as GPIO

			GPIO.setmode(GPIO.BCM)
			GPIO.setup(gpio_pins.GARAGE_OPENER, GPIO.OUT, initial=GPIO.HIGH)
			GPIO.output(gpio_pins.GARAGE_OPENER, GPIO.LOW)
			time.sleep(.1)
			GPIO.output(gpio_pins.GARAGE_OPENER, GPIO.HIGH)

		if self.log_event:
			entry = garage_log(user=self.user, action=1)
			entry.save()

	def toggle_light(self, pin, state):

		if pin not in [x for x, _ in lights_log.LIGHT_IDS]:
			return False

		if state not in [x for x, _ in lights_log.LIGHT_ACTIONS]:
			return False

		if self.gpio_enabled:
			import RPi.GPIO as GPIO

			if state == 1:
				signal_output = GPIO.LOW
			else:
				signal_output = GPIO.HIGH

			GPIO.setmode(GPIO.BCM)
			GPIO.setup(pin, GPIO.OUT, initial=signal_output)
			#GPIO.output(pin, signal_output)

		if self.log_event:
			entry = lights_log(user=self.user, light_id=pin, action=state)
			entry.save()

		return True


class sense_events():

	def __init__(self, user=None, log_event=True):

		self.user = user
		self.log_event = log_event

		try:
			import RPi.GPIO as GPIO
			self.gpio_enabled = True
		except (RuntimeError, ImportError, NameError):
			self.gpio_enabled = False

	def sense_garage_open(self):

		#return True if open, False if closed

		rtn = 'unknown'
		stat = 3

		if self.gpio_enabled:

			import RPi.GPIO as GPIO

			GPIO.setmode(GPIO.BCM)
			GPIO.setup(gpio_pins.GARAGE_SENSOR_UP, GPIO.IN)
			GPIO.setup(gpio_pins.GARAGE_SENSOR_DOWN, GPIO.IN)

			#if the garage is up the garage up senson will be 0
			garage_up = not bool(GPIO.input(gpio_pins.GARAGE_SENSOR_UP))

			#if the garage is down the garage down senson will be 0
			garage_down = not bool(GPIO.input(gpio_pins.GARAGE_SENSOR_DOWN))

			if garage_up:
				if not garage_down:
					rtn = 'true'
					stat = 1
				else:
					rtn = 'unknown'
					stat = 3

			if garage_down:
				if not garage_up:
					rtn = 'false'
					stat = 2
				else:
					rtn = 'unknown'
					stat = 3

		if self.log_event:
			entry = garage_log(user=self.user, action=2, result=stat)
			entry.save()

		return rtn

	def sense_light(self, pin):

		if pin not in [x for x, _ in lights_log.LIGHT_IDS]:
			return False

		state = 2

		if self.gpio_enabled:
			import RPi.GPIO as GPIO

			try:
				GPIO.setmode(GPIO.BCM)
				state = 2 if GPIO.input(pin) else 1
			except RuntimeError:
				pass
		if self.log_event:
			entry = lights_log(user=self.user, light_id=pin, action=3, result=state)
			entry.save()

		return state

