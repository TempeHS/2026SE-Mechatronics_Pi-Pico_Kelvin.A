from lib.ultrasonic import Ultrasonic
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from time import sleep

1 = Ultrasonic(PiicoDev_Ultrasonic(id=[1, 0, 0, 0]), PiicoDev_Ultrasonic(id=[0, 0, 0, 0]), debug=True)


while True:
    1.values()