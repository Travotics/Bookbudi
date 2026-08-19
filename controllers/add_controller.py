import json
from typing import List
from pathlib import Path

from fastapi import HTTPException
from sqlalchemy import select
from models.book_model import Book
from models.user_model import User
from schema.book_schema import BookCreate, BookResponse, GetBook
from schema.state_schema import StateSchema
from schema.district_schema import DistrictSchema
from sqlalchemy.ext.asyncio import AsyncSession

JSON_FILE = Path(__file__).parent.parent / "india_states_and_districts.json"

with open(JSON_FILE, "r", encoding="utf-8") as file:
    locations = json.load(file)

async def get_states() -> List[StateSchema]:

    # JSON_FILE = Path(__file__).parent.parent / "india_states_and_districts.json"

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        locations = json.load(file)
        return [
            {
              "id": item["id"],
              "name": item["name"]
            }
            for item in locations
            ]


async def get_districts(state:str) -> List[DistrictSchema]:
    for item in locations:

        if item["name"].lower() == state.lower():
            return item["districts"]

    raise HTTPException(
        status_code=404,
        detail="District not found"
    )

async def upload_bookdata(bookData: BookCreate, decoded_token: dict, db: AsyncSession) -> BookResponse:

    user_query = select(User).where(User.firebase_uid == decoded_token["uid"])
    result = await db.execute(user_query)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    book = Book(
        user_id = user.id,  
        category_id = bookData.category_id,
        book_name = bookData.book_name,
        image_urls = bookData.image_urls,
        condition = bookData.condition,
        state = bookData.state,
        city = bookData.city,
        address = bookData.address,
        price = bookData.price,
        note = bookData.note,
        phone_number = bookData.phone_number,
    )

    db.add(book)

    await db.commit()
    await db.refresh(book)

    return BookResponse(message="Book posted successfully")
