from Movement import ServoMovement
from time import sleep_ms

movement = ServoMovement(
    forward=(2500, 500),
    left=(500, 500),
    right=(2500, 2500),
    reverse=(500, 2500),
    stop=(1500, 1500)
)

movement.forward()
sleep_ms(1500)
movement.left()
sleep_ms(1500)
movement.right()
sleep_ms(1500)
movement.reverse()
sleep_ms(1500)
movement.stop()
sleep_ms(3000)
