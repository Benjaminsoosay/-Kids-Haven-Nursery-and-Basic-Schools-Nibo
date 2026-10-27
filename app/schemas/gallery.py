from pydantic import BaseModel


class GalleryImageCreate(BaseModel):
    title: str
    description: str
    image_url: str
    category: str


class GalleryImageResponse(GalleryImageCreate):
    id: str
