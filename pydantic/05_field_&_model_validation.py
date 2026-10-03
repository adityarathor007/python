from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str
    password: str
    confirm_password: str

    # does custom field checks if you want
    @field_validator('username') 
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("Username must be at least 4 characters!")
        return v;

    #used to validate using 2 or more fields 
    @model_validator(mode='after')
    def password_match(self):
        if self.password!=self.confirm_password:
            raise ValueError("Password dont match")
        return self

