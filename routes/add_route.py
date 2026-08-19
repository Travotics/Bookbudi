from typing import List

from fastapi import APIRouter,Depends,status

from auth import get_current_user
from controllers.add_controller import get_states, get_districts, upload_bookdata
from db.database import get_db
from schema.book_schema import BookCreate, BookResponse, GetBook
from schema.state_schema import StateSchema
from schema.district_schema import DistrictSchema
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api/v1", tags=["AddListing"])

@router.get(
    '/location/states',
    response_model = List[StateSchema],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all Indian states.",
)
async def fetch_states():
    return await get_states()


@router.get("/location/districts/{state}",
    response_model = List[DistrictSchema],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all Indian cities based on States"
)
async def fetch_districts(state: str):
    return await get_districts(state)


@router.post("/book",
    response_model = BookResponse,
    status_code = status.HTTP_201_CREATED,
    summary = "Post the book"
)
async def add_book( bookData: BookCreate,
                   decoded_token: dict = Depends(get_current_user),
                   db: AsyncSession = Depends(get_db),
):
    return await upload_bookdata(bookData,decoded_token,db)

    
    
