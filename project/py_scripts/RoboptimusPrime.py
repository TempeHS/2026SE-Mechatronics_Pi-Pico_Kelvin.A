import time
from machine import Pin, PWM
from servo import Servo


L_servo_pwm = PWM(Pin(16))
R_servo_pwm = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

l_servo = Servo(
    pwm=L_servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)
r_servo = Servo(
    pwm=R_servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

while True:
    r_servo.set_duty(500)
    l_servo.set_duty(2500)