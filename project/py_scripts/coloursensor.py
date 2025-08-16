from PiicoDev_VEML6040 import PiicoDev_VEML6040

class ColourSensor:
    def __init__(self, coloursensor, debug=False):
        self.__sensor = coloursensor
        self.__debug = debug

    def sensecolour(self):
        rgb = self.__sensor.readRGB()
        if self.__debug:
            print(f'RGB: {rgb}')

colourSensor = PiicoDev_VEML6040()

colour = ColourSensor(colourSensor, debug=True)
rgb = colour.sensecolour()
print(f"RGB: {rgb}")
