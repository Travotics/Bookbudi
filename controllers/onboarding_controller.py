from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.onboarding_model import OnboardingScreen

async def get_onboarding_slides(db: AsyncSession) -> List[OnboardingScreen]:
  
    # 1. Construct the async SQL SELECT query
    stmt = select(OnboardingScreen).where(OnboardingScreen.active == True)
    
    # 2. Execute the query using the injected database session
    result = await db.execute(stmt)

    # 3. Extract and return the ORM objects
    return result.scalars().all()