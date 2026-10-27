from beanie import Document


class GalleryImage(Document):
    title: str
    description: str
    image_url: str
    category: str

    class Settings:
        name = "gallery_images"
