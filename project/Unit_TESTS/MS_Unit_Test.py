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
    print('Robot should turn left')
    movement.left()
    sleep_ms(800)
    print('Robot should stop moving')
    movement.stop()
    sleep_ms(600)
    print('Robot should turn right')
    movement.right()
    sleep_ms(1000)
    print('Robot should move forward')
    movement.forward()
    break

