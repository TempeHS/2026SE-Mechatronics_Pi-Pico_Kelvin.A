from lib.colourscreen import ColourScreen
from PiicoDev_VEML6040 import PiicoDev_VEML6040


sensor = PiicoDev_VEML6040()
cs = ColourScreen(sensor, debug=True)

while True:
    hsv = cs.sensecolour()
    print(f'rgb: {hsv}')
    print('Hue value should show in Terminal')

