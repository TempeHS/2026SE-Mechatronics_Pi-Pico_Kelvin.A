from PiicoDev_VEML6040 import PiicoDev_VEML6040

class ColourSensor:
    def __init__(self):
        self.__sensor = PiicoDev_VEML6040()

    def read_rgb(self):
        return self.__sensor.read()

    def colour(self):
        r, g, b = self.read_rgb()
        if r > g and r > b:
            return "Red"
        elif g > r and g > b:
            return "Green"
        elif b > r and b > g:
            return "Blue"
        else:
            return "Idk"
