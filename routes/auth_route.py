from typing import List

from fastapi import APIRouter,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession

from auth import get_current_user
from controllers.login_controller import login
from db.database import get_db
from schema.user_schema import UserSchema

router = APIRouter(prefix="/api/v1", tags=["Authentication"])

@router.post(
    '/auth/login',
    response_model = UserSchema,
    status_code = status.HTTP_200_OK,
    summary = "Authenticate users",
)
async def user_login(db: AsyncSession = Depends(get_db),
                     decoded_token: dict = Depends(get_current_user)):
    return await login(db, decoded_token)