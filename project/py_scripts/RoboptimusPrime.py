from servomovement import ServoMovement
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from time import sleep_ms


movement = ServoMovement(
    forward=(2500, 500),
    left=(500, 500),
    right=(2500, 2500),
    reverse=(500, 2500),
    stop=(1500, 1500)
)

range_Front = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_Right = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

while True:
    distance_A = range_Front.distance_mm
    distance_B = range_Right.distance_mm
    movement.forward()
    print(distance_A, distance_B)
    

