from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db

router = APIRouter(tags=["Health"])

@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/ready")
async def ready(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ready"}

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )