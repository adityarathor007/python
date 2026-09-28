# a method that is bound to the class itself rather than its individual object instances. . 
# It can access and modify the class state, affecting all instances of that class. [if the object is not overriding the instance ]

class Car:
    origin="Germany"
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    
    @classmethod
    def from_dict(cls,car_data):
        return cls(
            car_data["model"],car_data["year"],car_data["price"]
        )

    @classmethod
    def from_str(cls,text):
        model,year,price=text.split("-")
        return cls(model,year,price)
    
    @classmethod
    def modifyOrigin(cls,country):
        cls.origin=country
    



car1=Car.from_dict({"model": "MercedesEClass","year":"2022","price":"56l"})
car2=Car.from_str("RangeRoverEvoque-2024-92l")
car3=Car("Mclaren","2026","2.3Cr")
Car.modifyOrigin("India")
print(car1.origin)