from pydantic import BaseModel

class DistrictSchema(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models