from Car import Car
import random
class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, realiability=0):
        super().__init__(name,fuel)
        self.realiability=realiability

    def __str__(self):
        return f"{super().__str__()}"
    def drive(self, distance):
        random_realiability = random.random()*100
        if random_realiability < self.realiability:
            distance_drive = super().drive(distance)
        else:
            distance_drive = 0
            print("Realiability error")
        return(distance_drive)