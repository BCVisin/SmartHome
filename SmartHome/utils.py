import gpio_pins
import time
import random


class trigger_events():

	def __init__(self):

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
			GPIO.cleanup()


class sense_events():

	def __init__(self):

		try:
			import RPi.GPIO as GPIO
			self.gpio_enabled = True
		except (RuntimeError, ImportError, NameError):
			self.gpio_enabled = False

	def sense_garage_open(self):

		#return True if open, False if closed

		if self.gpio_enabled:
			#if the garage is up the garage up senson will be 0
			garage_up = not bool(GPIO.input(gpio_pins.GARAGE_SENSOR_UP))

			#if the garage is down the garage down senson will be 0
			garage_down = not bool(GPIO.input(gpio_pins.GARAGE_SENSOR_DOWN))

			if garage_up:
				if not garage_down:
					return 'true'
				else:
					return 'unknown'

			if garage_down:
				if not garage_up:
					return 'false'
				else:
					return 'unknown'

		return 'unknown'

