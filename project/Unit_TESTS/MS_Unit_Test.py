from lib.servomovement import ServoMovement
from time import sleep_ms

movement = ServoMovement(
    forward=(2500, 500),
    left=(1500, 500),
    right=(2500, 2500),
    reverse=(500, 2500),
    stop=(1500, 1500)
)
while True:
    movement.left()
    sleep_ms(800)
    movement.stop()
    sleep_ms(600)
    movement.right()
    sleep_ms(1000)
    movement.forward()
    break

