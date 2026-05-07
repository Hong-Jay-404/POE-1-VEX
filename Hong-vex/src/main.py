# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Jenni                                                        #
# 	Created:      5/5/2026, 9:39:11 AM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #
"""
Name: main.py
Authors: Shoshana Howard and Jay Hong
Desciption: 
Date: 5/6/26
"""

from vex import *
 
 #Brain should be defined by default
brain=Brain()

# robot configuration
rightMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1,False) #right drivetrain motor
leftMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1,True) #left drivetrain motor
#set the leftMotor to reverse that when driving forward (or reversed) both motors will spin in the same direction
liftMotor = Motor(Ports.PORT3, GearSetting.RATIO_36_1,False) #liftarm
inertial_1 = Inertial(Ports.PORTS) #inertial sensor
bumpSwitch = Bumper(brain.three_wire_port.a) #bumper
#------------------
#Helper functions
def bump():
    """
    Hold the program's execution until the button is pressed
    """

    while(bumpSwitch.pressing()==False):
        wait(10, MSEC) #debounce the button 10 ms

        brain.screen.set_cursor(1,1) #sets the cursor to row 1, column 1
        brain.screen.print("Press the button to start the program")

        brain.screen.clear_line(1) #clears text in row 1
        brain.secreem.set_cursor(1,1) #sets the cursor to row 1, column 1
        brain.screen.print("Program exectued")
        wait(1,SECONDS)

#define main function
def main():
    bump() #call bump to execute program

main()


