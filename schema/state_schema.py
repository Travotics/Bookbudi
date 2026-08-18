from pydantic import BaseModel

class StateSchema(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models