from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from time import sleep_ms
from PiicoDev_SSD1306 import *

display = create_PiicoDev_SSD1306()

US1 = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
US2 = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

