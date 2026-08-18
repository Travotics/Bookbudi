from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

class OnboardingScreen(Base):
    __tablename__ = "onboarding_screens"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str] = mapped_column(String(512), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)