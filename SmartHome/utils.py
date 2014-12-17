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
			pass

		#for now, return a random boolean
		return bool(random.getrandbits(1))


