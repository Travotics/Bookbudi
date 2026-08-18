from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from schema.onboarding_schema import OnboardingItem
from schema.category_schema import Categories
from controllers.onboarding_controller import get_onboarding_slides

router = APIRouter(prefix="/api/v1", tags=["Onboarding"])

@router.get(
    '/onboarding',
    response_model = List[OnboardingItem],
    status_code = status.HTTP_200_OK,
    summary = "Fetch all active onboarding screens",
)
async def fetch_onboarding_data(db: AsyncSession = Depends(get_db)):
    return await get_onboarding_slides(db)
