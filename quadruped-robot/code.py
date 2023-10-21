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

#define the min and max degrees per leg segment
calf_min=25
calf_max=75
thigh_min=45
thigh_max=135

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.


def move_limb(thigh, calf):
    #pass in the int numbers for the thigh motor and leg motor 

    #thigh is outer loop, calf is inner
    for degree in range(calf_min, calf_max, 5):
        legs.servo[thigh].angle=degree
        time.sleep(1)
        legs.servo[calf].angle=degree

    return

legs = ServoKit(channels=8)

legs.servo[0].angle = 45
time.sleep(1)
legs.server[0].angle = 30
time.sleep(1)
