class ColourSensor:
    def __init__(self, coloursensor, debug=False):
        self.__coloursensor = coloursensor
        self.__debug = debug

    def sensecolour(self):
        hsv = self.__coloursensor.readHSV()
        red = hsv['red']
        green = hsv['green']
        blue = hsv['blue']
        if self.__debug:
            print(red, green, blue)

        return red, green, blue