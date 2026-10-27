from pydantic import BaseModel
from typing import Optional


class StaffCreate(BaseModel):
    full_name: str
    role: str
    qualification: str
    bio: str
    photo_url: str
    is_headteacher: bool = False


class StaffResponse(StaffCreate):
    id: str  # Maps to MongoDB's _id
