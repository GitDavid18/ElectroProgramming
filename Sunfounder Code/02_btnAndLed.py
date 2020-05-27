#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LedPin = 17 
BtnPin = 18

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
	if Led_status == 1:
		print ("led off...")
	else:
		print ("...led on")

def loop():
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed, bouncetime=200) # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
	while True:
		time.sleep(1)   # Don't do anything

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

