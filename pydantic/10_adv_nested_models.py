from typing import List,Optional
from pydantic import BaseModel


#Optional Nested Models
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None



#Mixed DataTypes
class TextContent(BaseModel):
    type: str="text"
    content: str

class ImageContent(BaseModel):
    type: str="Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]