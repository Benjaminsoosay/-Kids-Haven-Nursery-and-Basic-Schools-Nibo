from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.models.contact import ContactMessage
from app.models.school_info import SchoolInfo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# 1. This shows the Contact page (GET)
@router.get("/contact")
async def contact_page(request: Request):
    school = await SchoolInfo.find_one()
    return templates.TemplateResponse(
        request=request, name="contact.html", context={"school": school}
    )


# 2. This handles the form submission (POST)
@router.post("/contact")
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
):
    # Save the message to MongoDB
    new_message = ContactMessage(
        name=name, email=email, phone=phone, subject=subject, message=message
    )
    await new_message.insert()

    # Redirect back to the contact page with a success message
    return RedirectResponse(url="/contact?success=true", status_code=303)
