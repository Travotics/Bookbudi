from pydantic import BaseModel, HttpUrl

class OnboardingItem(BaseModel):
    title: str
    description: str
    image_url: HttpUrl

    class Config:
        from_attributes = True  # Allows ORM compatibility if loading from SQLAlchemy models