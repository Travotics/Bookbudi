from typing import List

from fastapi import APIRouter,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from controllers.categories_controller import get_categories
from db.database import get_db
from schema.category_schema import Categories

router = APIRouter(prefix="/api/v1", tags=["Categories"])

@router.get(
    '/categories',
    response_model = List[Categories],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all active categories",
)
async def fetch_categories(decoded_token: dict = Depends(get_current_user)
                           ,db: AsyncSession = Depends(get_db)):
    return await get_categories(db, decoded_token)