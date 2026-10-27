from beanie import Document


class Staff(Document):
    full_name: str
    role: str
    qualification: str
    bio: str
    photo_url: str
    is_headteacher: bool = False

    class Settings:
        name = "staff"
