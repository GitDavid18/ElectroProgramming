import time
import RPi.GPIO as GPIO
from enum import IntEnum

LedRed = 20
LedYellow = 21
LedGreen = 27

class SetOfLights(IntEnum):
    RED    = 1 << 0
    YELLOW = 1 << 1
    GREEN  = 1 << 2

def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
    GPIO.setup(LedRed, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedRed, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
    GPIO.setup(LedYellow, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedYellow, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
    GPIO.setup(LedGreen, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedGreen, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
    
def destroy():
    GPIO.output(LedRed, GPIO.HIGH)     # led off
    GPIO.output(LedYellow, GPIO.HIGH)     # led off
    GPIO.output(LedGreen, GPIO.HIGH)     # led off
    
    GPIO.cleanup()                     # Release resource

def main():
    keepRunning = True

    for x in range(2):
        lightStatus = 0b111 #all lights on
        GPIO.output(LedRed, GPIO.LOW)  # led on
        GPIO.output(LedYellow, GPIO.LOW)  # led on
        GPIO.output(LedGreen, GPIO.LOW)  # led on
        print('LightStatus: {:#05b}'.format(lightStatus))
        time.sleep(3)

        lightStatus = 0b000 #all lights off
        GPIO.output(LedRed, GPIO.HIGH) # led off
        GPIO.output(LedYellow, GPIO.HIGH) # led off
        GPIO.output(LedGreen, GPIO.HIGH) # led off
        print('LightStatus: {:#05b}'.format(lightStatus))
        time.sleep(3)

    lightStatus = SetOfLights.RED
    print('LightStatus: {:#05b}'.format(lightStatus))
    while keepRunning:
        msg = input('Switch lights?')
        
        if msg == 'end':
            keepRunning = False
            break
        
        if lightStatus is SetOfLights.RED:
            lightStatus |=  SetOfLights.YELLOW
            
            print('LightStatus: {:#05b}'.format(lightStatus))
            time.sleep(1)
            lightStatus = SetOfLights.GREEN


        elif lightStatus is SetOfLights.GREEN:
            lightStatus = SetOfLights.YELLOW
            print('LightStatus: {:#05b}'.format(lightStatus))
            time.sleep(2)
            lightStatus = SetOfLights.RED

        time.sleep(1)
        print('LightStatus: {:#05b}'.format(lightStatus))

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
