# Objective of pydantic is to avoid uncessary errors 
# used in data parsing, validation, serialization/deserialization, API Dev, config management


from pydantic import BaseModel

#give the type annotations
class User(BaseModel):
    id: int
    name: str
    is_active:bool

input_data={'id':101,'name':'Tom','is_active':True}

#Model init
user=User(**input_data) #pass after unpacking the dictonary 
print(user)
