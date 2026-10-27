from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config import settings

# Import all models (including User)
from app.models import SchoolInfo, Staff, GalleryImage, ContactMessage, User


async def init_db():
    client = AsyncIOMotorClient(settings.mongodb_uri)
    await init_beanie(
        database=client[settings.mongodb_db_name],
        document_models=[
            SchoolInfo,
            Staff,
            GalleryImage,
            ContactMessage,
            User,  # <-- Added User here!
        ],
    )
