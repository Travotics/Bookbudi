import os
from typing import AsyncGenerator
from config import settings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = settings.DB_URL

if not DATABASE_URL:
    raise ValueError("DB_URL environment variable is not set in .env file")

# Ensure correct driver for async engines (e.g. postgresql -> postgresql+asyncpg)
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Toggle SQL logging based on environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()
DEBUG_LOGS = os.getenv("SQL_ECHO", "false").lower() == "true" or ENVIRONMENT == "development"

# Configure Async Engine with pooling options
engine = create_async_engine(
    DATABASE_URL,
    echo=DEBUG_LOGS,
    pool_size=int(os.getenv("DB_POOL_SIZE", "10")),
    max_overflow=int(os.getenv("DB_MAX_OVERFLOW", "20")),
    pool_timeout=int(os.getenv("DB_POOL_TIMEOUT", "30")),
    pool_recycle=int(os.getenv("DB_POOL_RECYCLE", "1800")), # Recycle connections after 30 mins
    pool_pre_ping=True,  # Proactively test connections to prevent stale connection errors
)

# Configure session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


# Modern SQLAlchemy 2.0 Base model
class Base(DeclarativeBase):
    pass


# Database session dependency generator with error handling
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for providing a database session to API endpoints.

    Ensures proper rollback on failure and explicit closing on completion.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()