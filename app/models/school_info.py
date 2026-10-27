from beanie import Document
from typing import Optional


class SchoolInfo(Document):
    school_name: str = "Kids Haven Nursery and Basic Schools Nibo"
    motto: str = "Excellence through Godly discipline and Hard Work"
    email: str = "KidsHavennbibo@gmail.com"
    phone1: str = "08038588876"
    phone2: str = "08031177588"
    address: str = "Umuezeafugo Hall, Beside Ella Bread Factory, Ezeawulu Village, Nibo"
    vision: Optional[str] = None
    mission: Optional[str] = None
    curriculum: Optional[str] = None
    learning_environment: Optional[str] = None
    staff_description: Optional[str] = None
    logo_url: str = "/static/images/logo.png"

    class Settings:
        name = "school_info"
