from typing import List

from fastapi import APIRouter,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from controllers.home_controller import fetch_book_data, get_fests
from db.database import get_db
from schema.fest_schema import Fest
from schema.book_schema import GetBook

router = APIRouter(prefix="/api/v1", tags=["Home"])

@router.get(
    '/fest',
    response_model = List[Fest],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all ongoing and upcoming fests.",
)
async def fetch_fest(decoded_token: dict = Depends(get_current_user),
                     db: AsyncSession = Depends(get_db)):
    return await get_fests(db, decoded_token)



@router.get("/books",
    response_model = List[GetBook],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all books"
)
async def fetch_book(decoded_token: dict = Depends(get_current_user),
                     db: AsyncSession = Depends(get_db),
):
    return await fetch_book_data(decoded_token, db)
