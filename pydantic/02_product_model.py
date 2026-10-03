from pydantic import BaseModel

#give the type annotations
class Product(BaseModel):
    id: int
    name: str
    price:float
    in_stock:bool=True #has a default value

product_one=Product(id=1,name="Laptop",price=999.99,in_stock=True)
product_two=Product(id=2,name="Mouse",price=24)
product_two=Product(id=3,name="Keyboard",price=57)
    

