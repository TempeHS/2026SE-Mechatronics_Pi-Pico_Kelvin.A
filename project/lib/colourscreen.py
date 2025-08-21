from PiicoDev_VEML6040 import PiicoDev_VEML6040

class ColourScreen:
    def __init__(self, coloursensor, debug=False):
        self.__coloursensor = coloursensor
        self.__debug = debug

    def sensecolour(self):
        hsv = self.__coloursensor.readHSV()
        if self.__debug:
            print(hsv)
        return hsv

