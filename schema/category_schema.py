from pydantic import BaseModel, HttpUrl

class Categories(BaseModel):
    id:int
    title: str
    image_url: HttpUrl
    active: bool

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models