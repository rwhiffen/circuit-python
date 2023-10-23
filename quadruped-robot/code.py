# Rich Whiffen - 10/09/2023
#
# Getting started trying to get the board to work
# 
# it looks like I have the wrong feather board...
# so this is stalled out
#
# 10/14/23 - turns out I have a feather M4 to play with 
#            game on!
#

import time
from adafruit_servokit import ServoKit
from digitalio import DigitalInOut, Direction, Pull


SWITCH_PIN = board.D9 # put a switch on D9 for the action button

#define the min and max degrees per leg segment
#not sure I'm going to use this - this may get thrown away later
calf_min=25
calf_max=75
calf_start=(calf_min + calf_max)/2
thigh_min=45
thigh_max=135
thigh_start=(thigh_min + thigh_max)/2

switch = DigitalInOut(SWITCH_PIN)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

def move_limb(thigh, calf):
    #pass in the int numbers for the thigh motor and leg motor 

    #thigh is outer loop, calf is inner
    for degree in range(calf_min, calf_max, 5):
        legs.servo[thigh].angle=degree
        time.sleep(1)
        legs.servo[calf].angle=degree

    return

def ready_posture():
    #loop through each servo and set it to a default, known angle
    for limb in range(0, 8): #the last one - 8, never gets hit
        if limb % 2 == 1:        
            legs.servo[limb].angle=calf_start 
        if limb % 2 == 0:        
            legs.servo[limb].angle=thigh_start 
    
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
legs = ServoKit(channels=8)



# Main program loop, repeats indefinitely

while True:
    if not switch.value:                    # button pressed?
        #if button was pressed, lets move a limb:
        legs.servo[0].angle = 45
        time.sleep(1)
        legs.server[0].angle = 30
        time.sleep(1)
