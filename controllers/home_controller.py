from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.fest_model import Fests

async def get_fests(db: AsyncSession, decoded_token: dict) -> List[Fests]:
  
    # 1. Construct the async SQL SELECT query
    stmt = select(Fests).where(Fests.active == True)
    
    # 2. Execute the query using the injected database session
    result = await db.execute(stmt)

    # 3. Extract and return the ORM objects
    return result.scalars().all()