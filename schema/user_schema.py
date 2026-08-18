from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    firebase_uid: str
    role:str
    username: str
    email:str
    phone:str
    profile_image:str
    active: bool
    created_at: str

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models