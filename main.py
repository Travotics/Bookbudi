from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.database import engine, Base
from firebase_config import initialize_firebase
from routes.onboarding_route import router as onboarding_router
from routes.category_route import router as category_router
from routes.home_route import router as home_router
from routes.auth_route import router as auth_router
from routes.add_route import router as add_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP LOGIC ---
    async with engine.begin() as conn:
        # Creates all tables that inherit from Base if they don't already exist
        await conn.run_sync(Base.metadata.create_all)

        # Initialize Firebase Admin SDK
        initialize_firebase()
    
    yield  # The app runs while paused here
    
    # --- SHUTDOWN LOGIC ---
    # Clean up connection pool on server shutdown
    await engine.dispose()

app = FastAPI(title="Bookbudi APIs", lifespan=lifespan)

app.include_router(onboarding_router)
app.include_router(category_router)
app.include_router(home_router)
app.include_router(auth_router)
app.include_router(add_router)

@app.get("/")
async def root():
    return {"message": "Bookbudi API is running"}
