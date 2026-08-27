from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.database import engine, Base
from firebase_config import initialize_firebase
from routes.onboarding_route import router as onboarding_router
from routes.category_route import router as category_router
from routes.home_route import router as home_router
from routes.auth_route import router as auth_router
from routes.add_route import router as add_router
from routes.health_route import router as health_router

from config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP LOGIC ---
    # async with engine.begin() as conn:
        # Creates all tables that inherit from Base if they don't already exist
        # await conn.run_sync(Base.metadata.create_all)

        # Initialize Firebase Admin SDK
    initialize_firebase()
    
    yield  # The app runs while paused here
    
    # --- SHUTDOWN LOGIC ---
    # Clean up connection pool on server shutdown
    await engine.dispose()

title = "Bookbudi APIs(Dev)" if settings.APP_ENV == "dev" else "Bookbudi APIs(Prod)"
app = FastAPI(title=title, lifespan=lifespan)

app.include_router(onboarding_router)
app.include_router(category_router)
app.include_router(home_router)
app.include_router(auth_router)
app.include_router(add_router)
app.include_router(health_router)

@app.get("/")
async def root():
    return {"message": f"Bookbudi APIs are running in {settings.APP_ENV}"}
