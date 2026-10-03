from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price:float
    quantity: int

    @computed_field #to calculate the attribute on-the-go when called
    @property #to make it accessible like other fields
    def total_price(self) -> float:
        return self.price*self.quantity


prd=Product(
    price=12,
    quantity=24
)

print(prd.total_price)
print(prd.model_dump())  #primary way of converting a model to dictionary. Sub-models will be recursivelly converted to dictonaries
print("="*30)
print(prd.model_dump_json())  #converting to json encode string (data encoded in string)