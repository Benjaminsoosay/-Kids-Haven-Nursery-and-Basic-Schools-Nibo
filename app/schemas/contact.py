from pydantic import BaseModel, EmailStr, Field


class ContactCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    subject: str = Field(..., min_length=3, max_length=150)
    message: str = Field(..., min_length=10)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "phone": "08012345678",
                "subject": "School Fees Enquiry",
                "message": "Hello, I would like to know the tuition fees for Nursery 1.",
            }
        }
