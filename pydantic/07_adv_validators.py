from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name:str
    last_name: str

    @field_validator('first_name','last_name') #same validators for multiple fields
    def names_must_be_capitalized(cls,v):
        if not v.istitle():
            raise ValueError("Names must be capitalized")
        return v

    @field_validator('first_name')
    def normalize_email(cls,v):
        return v.lower().strip()
    

class Product(BaseModel):
    price: str #$4.44
    
    #even before pydantic does the validation and takes the input and converts to float which is later converted by pydantic to str
    @field_validator('price', mode='before') 
    def parse_price(cls,v):
        if isinstance(v,str):
            return float(v.replace('$','').replace(',',''))
        return v 

class DateRange(BaseModel):
    start_date: datetime
    end_date:datetime
    
    @model_validator(mode="after")
    def validate_date_range(self):
        if self.start_date>self.end_date:
            raise ValueError("end date must be greater than start date")
        return self