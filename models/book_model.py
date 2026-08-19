from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ARRAY, Boolean, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base

if TYPE_CHECKING:
    from models.category_model import Category
    from models.user_model import User

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False,index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"),nullable=False,index=True)
    book_name: Mapped[str] = mapped_column(nullable=False)
    image_urls: Mapped[list[str]] = mapped_column(ARRAY(String),nullable=False,default=list)
    condition: Mapped[str] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str | None] = mapped_column(nullable=True)
    note: Mapped[str | None] = mapped_column(nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(20),nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    user: Mapped["User"] = relationship(back_populates="books")
    category: Mapped["Category"] = relationship(
        lambda: __import__('models.category_model', fromlist=['Category']).Category, 
        back_populates="books"
    )