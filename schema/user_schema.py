from datetime import datetime   
from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    firebase_uid: str
    role:str
    username: str|None
    email:str
    phone_number:str|None
    profile_image:str|None
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models