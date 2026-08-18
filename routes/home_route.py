from typing import List

from fastapi import APIRouter,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from controllers.home_controller import get_fests
from db.database import get_db
from schema.fest_schema import Fest

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