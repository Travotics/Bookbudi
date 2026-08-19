from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class BookCreate(BaseModel):
    category_id: int
    book_name: str
    image_urls: list[str]
    condition: str
    state: str
    city: str
    address: str
    price: str
    note: str | None = None
    phone_number: str | None = None

class BookResponse(BaseModel):
    message: str

class GetBook(BaseModel):
    id: int
    user_id: int
    category_id: int
    category_name: str      
    book_name: str
    image_urls: List[str]
    condition: str
    state: str
    city: str
    address: str
    price: str
    note: Optional[str] = None
    phone_number: Optional[str] = None

