# Car IS-A Vehicle (inheritince) and Car HAS-A Engine (composition)

class Vehicle:
    def __init__(self,wheeler):
        self.wheeler=wheeler

    def start(self):
        print("Start the vehicle")

class Engine:
    def start(self):
        print("Engine started")


class ElectricEngine:
    def start(self):
        print("Electric motor started")


class Car(Vehicle):
    def __init__(self,wheeler,engine):
        super().__init__(wheeler)  #accessing the parent class 
        self.engine = engine

    def start_car(self):
        self.start()
        self.engine.start()
        print("Car started")


car=Car(4,Engine())
car.start_car()
ecar=Car(4,ElectricEngine())
ecar.start_car()