import math
from servo_ax12a import *

import time
        
# Class definition of ax12a-controller class, defines interface to the robot
#===============================================================================
# Implements the interface between leg- and servo class
# ------------------------------------------------------------------------------
# Provides all required methods that allow the leg class to control the servo
# Implements all nessesary codomain conversion between leg- and servo values
# Limits values too valid servo values
# Servo uses ticks from 0 to 1023 for angle and speed
# Leg uses angles in radian and rotation per minit for speed
# Defines zero angle as average of min- and max value -> positive and negativ angles are allowed
class JointDrive(ServoAx12a):

    # Definition of public class attributes
    #----------------------------------------------------------------------
    _ANGLE_RADIAN_ZERO = (ServoAx12a._ANGLE_MAX_DEGREE - ServoAx12a._ANGLE_MIN_DEGREE) * math.pi / 360  # Zero angle offset of servo in radian
    _ANGLE_UNIT = ServoAx12a._ANGLE_MAX_TICKS / ((ServoAx12a._ANGLE_MAX_DEGREE - \
                                                 ServoAx12a._ANGLE_MIN_DEGREE) * math.pi * 2 / 360)     # Ticks per rad
    
    # Private methods    
    #----------------------------------------------------------------------
    # Constructor, defines the folowing variables: counterClockWise, angleOffset, angleMax, angleMin
    # id -> id of servo, cw -> rotating direction, aOffset -> angle offset,
    # aMax -> maximum angle allowed, aMin -> minimum angle allowed
    def __init__(self, id, ccw = False, aOffset = 0.0, aMax = math.pi * 2, aMin = -math.pi * 2):
       pass 
    # Converts angle in radian to servo ticks
    # angle -> in radian, returns angle in servo ticks
    def __convertAngleToTicks(self, angle):
        pass
    # Converts servo ticks to angle in radian
    # ticks -> servo ticks, returns angle in radian
    def __convertTicksToAngle(self, ticks):
        pass
    # Converts speed in rpm to servo ticks
    # speed -> value in rpm
    def __convertSpeedToTicks(self, speed):
        pass
    # Converts ticks to speed in rpm
    # ticks -> servo ticks
    def __convertTicksToSpeed(self, ticks):
        pass
    # Public methods    
    #----------------------------------------------------------------------
    # Get current angle of servo
    # returns angle in radian
    def getCurrentJointAngle(self):
        pass
    # Set servo to desired angle
    # angle -> in radian,
    # speed -> speed of movement, speed < 0 -> no speed set, speed = 0 -> maximum speed
    def setDesiredJointAngle(self, angle, trigger = False):
        pass
    # Set servo to desired angle
    # angle -> in radian,
    # speed -> speed of movement in rpm, speed = 0 -> maximum speed
    def setDesiredAngleSpeed(self, angle, speed = 0, trigger = False):
        pass
    # Set speed value of servo
    # speed -> angle speed in rpm
    def setSpeedValue(self, speed, trigger = False):
        pass