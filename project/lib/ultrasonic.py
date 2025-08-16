from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

range_Front = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_Left = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

class Ultrasonic:
    def __init__(self, threshold=[100, 99, 101]):
        self.__threshold = [100, 99, 101]

    def values(self):
        if range_Front <= 
