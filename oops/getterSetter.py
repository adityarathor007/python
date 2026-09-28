class Car:
    def __init__(self,variant):
        self._variant=variant

    @property
    def variant(self):
        return self._variant+2
    
    @variant.setter
    def variant(self,variant):
        if 1<=variant<=5:
            self._variant=variant
        else:
            raise ValueError("Error: variant should be between 1 to 5")


car=Car(0)
print(car.variant) #calling the getter
car.variant=2  #calling the setter
print(car.variant)
