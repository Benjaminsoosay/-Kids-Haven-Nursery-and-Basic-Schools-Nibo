from pydantic import BaseModel, EmailStr
from typing import Optional


class SchoolInfoBase(BaseModel):
    school_name: str
    motto: str
    email: EmailStr
    phone1: str
    phone2: str
    address: str
    vision: Optional[str] = None
    mission: Optional[str] = None
    curriculum: Optional[str] = None
    learning_environment: Optional[str] = None
    staff_description: Optional[str] = None
    logo_url: Optional[str] = "/static/images/logo.png"


class SchoolInfoUpdate(BaseModel):
    # All fields are optional so you can update just one if you want
    school_name: Optional[str] = None
    motto: Optional[str] = None
    email: Optional[EmailStr] = None
    phone1: Optional[str] = None
    phone2: Optional[str] = None
    address: Optional[str] = None
    vision: Optional[str] = None
    mission: Optional[str] = None
    curriculum: Optional[str] = None
    learning_environment: Optional[str] = None
    staff_description: Optional[str] = None
    logo_url: Optional[str] = None
