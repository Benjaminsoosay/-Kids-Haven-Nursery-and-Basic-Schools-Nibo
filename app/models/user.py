from beanie import Document


class User(Document):
    full_name: str
    email: str
    password_hash: str
    role: str = "parent"  # Default role is parent

    class Settings:
        name = "users"
