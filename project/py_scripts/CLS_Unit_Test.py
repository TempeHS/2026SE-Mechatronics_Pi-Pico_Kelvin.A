from coloursensor import ColourSensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040


while True:
    sensor = PiicoDev_VENL6040()

    cs = ColourSensor(sensor, debug=True)

    rgb = cs.sensecolour()
    print(f'rgb: {rgb}')

