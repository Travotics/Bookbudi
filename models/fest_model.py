from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

class Fests(Base):
    __tablename__ = "fest"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    image_url: Mapped[str] = mapped_column(String(512), nullable=False)
    venue: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(255))
    start_date: Mapped[str] = mapped_column(String(512))
    end_date: Mapped[str] = mapped_column(String(512))
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)