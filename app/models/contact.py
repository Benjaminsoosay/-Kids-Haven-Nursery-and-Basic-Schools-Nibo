from beanie import Document
from datetime import datetime


class ContactMessage(Document):
    name: str
    email: str
    phone: str
    subject: str
    message: str
    date_sent: datetime = datetime.now()

    class Settings:
        name = "contact_messages"
