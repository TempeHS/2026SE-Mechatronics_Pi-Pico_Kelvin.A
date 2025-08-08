from machine import Pin, PWM
from servo import Servo

l_servo = Servo(PWM(Pin(16)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
r_servo = Servo(PWM(Pin(15)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)

class ServoMovement:
    def __init__(self, forward, left, right, reverse, stop):
        self.__forward = forward
        self.__left = left
        self.__right = right
        self.__reverse = reverse
        self.__stop = stop
        
    def forward(self):
        l_servo.set_duty(self.__forward[0])
        r_servo.set_duty(self.__forward[1])
    def left(self):
        l_servo.set_duty(self.__left[0])
        r_servo.set_duty(self.__left[1])
    def right(self):
        l_servo.set_duty(self.__right[0])
        r_servo.set_duty(self.__right[1])
    def reverse(self):
        l_servo.set_duty(self.__reverse[0])
        r_servo.set_duty(self.__reverse[1])
    def stop(self):
        l_servo.set_duty(self.__stop[0])
        r_servo.set_duty(self.__stop[1])