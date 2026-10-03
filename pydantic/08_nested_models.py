from typing import List
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address #custom type annotation 


# M1: creating 2 objects

# address=Address(
#     street="123 something",
#     city="Noida",
#     postal_code="402024"
# )
# user=User(
#     id=1,
#     name="XYZ",
#     address=address
# )

# M2: using dictonary
user_data={
    "id": 1,
    "name":"XYZ",
    "address": {
        "street": "123 something",
        "city": "Noida",
        "postal_code": "202421"
    }
}

user=User(**user_data)

print(user)