from datetime import datetime, timezone
from typing import List
from firebase_admin import auth
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user_model import User

async def login(db: AsyncSession, decoded_token: dict) -> User:

    firebase_uid = decoded_token["uid"]
    email = decoded_token.get("email")
    profile_image = decoded_token.get("picture")
    username = decoded_token.get("name")
    
    # Get Firebase account information
    firebase_user = auth.get_user(firebase_uid)
    created_at = datetime.fromtimestamp(firebase_user.user_metadata.creation_timestamp / 1000,
                                        tz=timezone.utc)

    result = await db.execute(select(User).where(User.firebase_uid == firebase_uid))

    user = result.scalar_one_or_none()

    if user is None:

        user = User(
            firebase_uid = firebase_uid,
            email = email,
            profile_image = profile_image,
            username = username,
            role = "user",
            created_at = created_at,
            active = True
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

    return user