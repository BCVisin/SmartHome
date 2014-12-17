import gpio_pins
import time

class trigger_events():

	def __init__(self):

		try:
			import RPi.GPIO as GPIO
			self.gpio_enabled = True
		except (RuntimeError, ImportError):
			self.gpio_enabled = False

	def toggle_garage_door(self):

		if self.gpio_enabled:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(gpio_pins.GARAGE_OPENER, GPIO.OUT, initial=GPIO.HIGH)
			GPIO.output(gpio_pins.GARAGE_OPENER, GPIO.LOW)
			time.sleep(.1)
			GPIO.output(gpio_pins.GARAGE_OPENER, GPIO.HIGH)
			GPIO.cleanup()

