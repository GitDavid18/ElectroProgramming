import time
from enum import IntEnum

class SetOfLights(IntEnum):
    RED    = 1 << 0
    YELLOW = 1 << 1
    GREEN  = 1 << 2

def main():
    keepRunning = True

    for x in range(2):
        lightStatus = 0b111 #all lights on 
        print('LightStatus: {:#05b}'.format(lightStatus))
        time.sleep(0.5)

        lightStatus = 0b000 #all lights off 
        print('LightStatus: {:#05b}'.format(lightStatus))
        time.sleep(0.5)

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
    main()
