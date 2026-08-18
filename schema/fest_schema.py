from pydantic import BaseModel, HttpUrl

class Fest(BaseModel):
    id:int
    name: str
    image_url: HttpUrl
    start_date: str
    end_date:str
    venue:str
    city:str
    active: bool

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models