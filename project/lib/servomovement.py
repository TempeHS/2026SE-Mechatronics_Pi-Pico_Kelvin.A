from machine import Pin, PWM
from servo import Servo
from time import sleep

class ServoMovement:
    def __init__(self, forward, left, right, reverse, stop, l_pin=16, r_pin=15):
        self.__l_servo = Servo(PWM(Pin(l_pin)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.__r_servo = Servo(PWM(Pin(r_pin)), min_us=500, max_us=2500, dead_zone_us=1500, freq=50)
        self.__forward = forward
        self.__left = left
        self.__right = right
        self.__reverse = reverse
        self.__stop = stop

    def forward(self):
        self.__l_servo.set_duty(self.__forward[0])
        self.__r_servo.set_duty(self.__forward[1])

    def left(self):
        self.__l_servo.set_duty(self.__left[0])
        self.__r_servo.set_duty(self.__left[1])

    def right(self):
        self.__l_servo.set_duty(self.__right[0])
        self.__r_servo.set_duty(self.__right[1])

    def reverse(self):
        self.__l_servo.set_duty(self.__reverse[0])
        self.__r_servo.set_duty(self.__reverse[1])

    def stop(self):
        self.__l_servo.set_duty(self.__stop[0])
        self.__r_servo.set_duty(self.__stop[1])
