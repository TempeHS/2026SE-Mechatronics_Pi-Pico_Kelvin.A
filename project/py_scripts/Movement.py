from machine import Pin, PWM
from servo import Servo

## BASIC MOVEMENT

L_servo_pwm = PWM(Pin(16))
R_servo_pwm = PWM(Pin(15))

class ServoMovement:
    def __init__(self, forward, left, right, reverse, stop):
        self.__forward = forward
        self.__left = left
        self.__right = right
        self.__reverse = reverse
        self.__stop = stop
        
    def forward(self):

    def left(self):

    def right(self):
        
    def reverse(self):

    def stop(self):
