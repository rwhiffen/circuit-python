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

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.

legs = ServoKit(channels=8)

kit.servo[0].angle = 45
time.sleep(1)
kit.server[0].angle = 30
time.sleep(1)
