from lib.servomovement import ServoMovement
from lib.coloursensor import ColourSensor
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_VEML6040 import PiicoDev_VEML6040
# from PiicoDev_SSD1306 import *
from time import sleep_ms


movement = ServoMovement(
    forward=(2500, 500),
    left=(500, 500),
    right=(2500, 2500),
    reverse=(500, 2500),
    stop=(1500, 1500)
)

# display = create_PiicoDev_SSD1306()


range_Front = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_Right = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

sensor = PiicoDev_VEML6040()
cs = ColourSensor(sensor, debug=True)

while True:
    hsv = cs.sensecolour()
    hue = hsv['hue']
    distance_A = range_Front.distance_mm
    distance_B = range_Right.distance_mm
    print(distance_A, distance_B)
    
    if hue > 90:
        movement.stop()
        sleep_ms(500)
        movement.forward()
        sleep_ms(400)
        continue

    if distance_A <= 100 and distance_B <= 100:
        movement.stop()
        sleep_ms(600)
        movement.left()
        sleep_ms(475)
        

    elif distance_A <= 100 and distance_B >= 101:
        movement.stop()
        sleep_ms(600)
        movement.right()
        sleep_ms(475)

    else:
        movement.forward()
    
    