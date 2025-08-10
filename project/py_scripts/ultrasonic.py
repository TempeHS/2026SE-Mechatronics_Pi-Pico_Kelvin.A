from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

range_Front = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_Left = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

class Ultrasonic:
    def __init__(self, threshold=500):
        self.threshold = threshold

    def stop(self):
        return range_Front.distance_mm <= self.threshold

    def turn_right(self):
        return range_Left.distance_mm == self.threshold

    def turn_left(self):
        return range_Left.distance_mm != self.threshold








