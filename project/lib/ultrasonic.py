from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

class Ultrasonic:
    def __init__(self, ultrasonic1, ultrasonic2, debug=False):
        self.__ultrasonic1 = ultrasonic1
        self.__ultrasonic2 = ultrasonic2
        self.__debug = debug

    def values(self):
        distance1 = self.__ultrasonic1.distance_mm()
        distance2 = self.__ultrasonic2.distance_mm()
        if self.__debug:
            print(distance1, distance2)
        return (distance1, distance2)
