from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

US1 = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
US2 = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

class UltraSonic():
    def __init__(self, US1, US2, debug=False):
        self.__US1 = US1
        self.__US2 = US2