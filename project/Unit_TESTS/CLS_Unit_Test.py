from lib.colorsensor import ColourSensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040


sensor = PiicoDev_VEML6040()
cs = ColourSensor(sensor, debug=True)

while True:
    hsv = cs.sensecolour()
    print(f'rgb: {hsv}')
    print('Hue value should show in Terminal')

