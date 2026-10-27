from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.database.mongodb import init_db
from starlette.middleware.sessions import SessionMiddleware  # <-- ADDED

# Import all routers (Added 'auth' to this line)
from app.routers import (
    home,
    about,
    admissions,
    contact,
    gallery,
    admin,
    auth,
)  # <-- ADDED AUTH


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB on startup
    await init_db()
    print("✅ Connected to MongoDB successfully!")
    yield
    # Add shutdown logic here if needed later


# Create FastAPI app
app = FastAPI(
    title="Kids Haven API",
    description="Backend API for Kids Haven Nursery and Basic Schools",
    version="1.0.0",
    lifespan=lifespan,
)

# Add Session Middleware (This allows users to stay logged in)
app.add_middleware(
    SessionMiddleware, secret_key="your-super-secret-key-change-me"
)  # <-- ADDED

# Mount static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include all routers
app.include_router(home.router)
app.include_router(about.router)
app.include_router(admissions.router)
app.include_router(contact.router)
app.include_router(gallery.router)
app.include_router(admin.router)
app.include_router(auth.router)  # <-- ADDED AUTH ROUTER


# A simple health check route to make sure the server is running
@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "API is running perfectly"}
