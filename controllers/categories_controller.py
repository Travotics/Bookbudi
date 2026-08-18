from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.category_model import Category
from models.category_model import Category

async def get_categories(db: AsyncSession, decoded_token: dict) -> List[Category]:
  
    # 1. Construct the async SQL SELECT query
    stmt = select(Category).where(Category.active == True)
    
    # 2. Execute the query using the injected database session
    result = await db.execute(stmt)

    # 3. Extract and return the ORM objects
    return result.scalars().all()