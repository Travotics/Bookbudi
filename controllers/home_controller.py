from typing import List
from alembic.util import status
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from auth import get_current_user
from db.database import get_db
from models.book_model import Book
from models.fest_model import Fests
from schema.book_schema import GetBook

async def get_fests(db: AsyncSession, decoded_token: dict) -> List[Fests]:
  
    # 1. Construct the async SQL SELECT query
    stmt = select(Fests).where(Fests.active == True)
    
    # 2. Execute the query using the injected database session
    result = await db.execute(stmt)

    # 3. Extract and return the ORM objects
    return result.scalars().all()


async def fetch_book_data(decoded_token: dict, db: AsyncSession) -> List[GetBook]:

    stmt = select(Book).options(selectinload(Book.category))
    result = await db.execute(stmt)
    books = result.scalars().all()

    # Build response list
    books_response = []

    for book in books:
        category_name = book.category.title if book.category else None
        # Create an instance of GetBook for each book
        book_response = GetBook(
            id=book.id,
            user_id=book.user_id,
            category_id=book.category_id,
            category_name=category_name,
            book_name=book.book_name,
            image_urls=book.image_urls,
            condition=book.condition,
            state=book.state,
            city=book.city,
            address=book.address,
            price=book.price,
            note=book.note,
            phone_number=book.phone_number,
        )
        books_response.append(book_response)

    return books_response
