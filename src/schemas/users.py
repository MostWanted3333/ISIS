

from pydantic import BaseModel,EmailStr


class UserAddSchema(BaseModel):
    full_name:str 
    email: EmailStr
    password_hash : str
    
class UserSchema(UserAddSchema):
    id:int 
