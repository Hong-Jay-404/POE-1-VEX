# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Shoshana Howard and Jay Hong                                                        #
# 	Created:      5/5/2026, 9:40:00 AM                                         #
# 	Description:  Code for POE RECbot activities                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
 
# Brain should be defined by default
brain=Brain()

# ------------------ Robot Configuration Code ------------------
rightMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1,False) #right drivetrain motor
leftMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1,True) #left drivetrain motor
# Set the leftMotor to reverse so that when driving forward (or reverse) it turns
# in the same direction as the right motor
liftMotor = Motor(Ports.PORT3, GearSetting.RATIO_36_1,False) # Liftarm motor
inertial_1 = Inertial(Ports.PORT5)                           # inertial sensor
bumpSwitch = Bumper(brain.three_wire_port.a)                 # bumper switch
#----------------------------------------------------------------
#------------------- Helper Functions ------------------
def bump():
    """
    Hold the program's execution until the button is pressed
    """

    while(bumpSwitch.pressing()==False):
        wait(10, MSEC) #debounce the button (10 ms)

        brain.screen.set_cursor(1,1) #place cursor in upper left corner
        brain.screen.print("Press the button to start the program")
        pass

    brain.screen.clear_line(1) #clears text in row 1
    brain.screen.set_cursor(1,1) #sets the cursor to row 1, column 1
    brain.screen.print("Program exectued")
    wait(1,SECONDS) #wait 1 second before proceeding

def inertialCalibration():
    """
    Calibrate the inertial sensor
    A wait time of 2 seconds is required
    This function should be called at the start of the program's execution
    """

    brain.screen.clear_screen() # Clear the brain's screen
    brain.screen.set_cursor(1,1)
    brain.screen.print("Calibrating the inertial sensor")
    brain.screen.set_cursor
    brain.screen.print("Don't move the robot!")
    inertial_1.calibrate() # Calibrate the inertial sensor

    wait(2, SECONDS) # Wait for the calibration to complete

    brain.screen.clear_line(1) # Clear the text on row 1
    brain.screen.set_cursor(1,1)
    brain.screen.print("Inertial sensor calibrated")

def testInertial():
    """
    Test the inertial sensor by having it display heading and total rotation 
    data. Pressing the bump switch will end the test.
    """

    brain.screen.clear_screen()
    while(bumpSwitch.pressing()==False):
       brain.screen.set_cursor(5,1)
       brain.screen.print("Heading: " + str(inertial_1.heading()))
       brain.screen.set_cursor(6,1)
       brain.screen.print("Rotation: " + str(inertial_1.rotation()))
       brain.screen.set_cursor(8,1)
       brain.screen.print("Press the button for the bump switch to exit")
       if (bumpSwitch.pressing() == True):
           break
       brain.screen.clear_line(8) 
       brain.screen.set_cursor(8,1)
       brain.screen.print("Inertial test terminated")

#------------------- Define main() function  ------------------
def main():
    """
    The main() function is the program that will be executer by the brain
    """
    bump()                # Call bump() to execute program
    inertialCalibration() # Calibrate the inertial sensor
    testInertial()        # Test the inertial's output

main()