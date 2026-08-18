from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base

if TYPE_CHECKING:
    from models.book_model import Book

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    firebase_uid: Mapped[str] = mapped_column(index=True, nullable=False, unique=True)
    role: Mapped[str] = mapped_column(String(255), nullable=False, default="user")
    username: Mapped[str | None] = mapped_column(String(512), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    phone_number: Mapped[str | None] = mapped_column(String(20),nullable=True)
    profile_image: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    books: Mapped[list["Book"]] = relationship(back_populates="user",cascade="all, delete-orphan")