#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

MotorPin1   = 17
MotorPin2   = 18
MotorEnable = 27

def setup():
	GPIO.setmode(GPIO.BCM)          # Numbers GPIOs by BCM
	GPIO.setup(MotorPin1, GPIO.OUT)   # mode --- output
	GPIO.setup(MotorPin2, GPIO.OUT)
	GPIO.setup(MotorEnable, GPIO.OUT)
	GPIO.output(MotorEnable, GPIO.LOW) # motor stop

def loop():
	while True:
		print ("Press Ctrl+C to end the program...")
		GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
		GPIO.output(MotorPin1, GPIO.HIGH)  # clockwise
		GPIO.output(MotorPin2, GPIO.LOW)
		time.sleep(5)
		
		GPIO.output(MotorEnable, GPIO.LOW) # motor stop
		time.sleep(5)
		
		GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
		GPIO.output(MotorPin1, GPIO.LOW)   # anticlockwise
		GPIO.output(MotorPin2, GPIO.HIGH)
		time.sleep(5)
		
		GPIO.output(MotorEnable, GPIO.LOW) # motor stop
		time.sleep(5)

def destroy():
	GPIO.output(MotorEnable, GPIO.LOW) # motor stop
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

