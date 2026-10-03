from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int,
    name: str=Field(
        ..., #means that this field is required 
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Hitesh Chaoudhary"
    )
    department:Optional[str]="General",
    salary: float=Field(
        ...,
        ge=10000
    )

