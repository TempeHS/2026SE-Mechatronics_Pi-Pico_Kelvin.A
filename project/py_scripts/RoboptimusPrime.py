import time
from machine import Pin, PWM
from servo import Servo
from servomovement import ServoMovement
from ultrasonic import UltrasonicSensor

movement = ServoMovement(
    forward=(2500, 500),
    left=(500, 500),
    right=(2500, 2500),
    reverse=(500, 2500),
    stop=(1500, 1500)
)






while True: