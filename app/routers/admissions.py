from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.models.school_info import SchoolInfo  # <-- ADDED: Import the SchoolInfo model

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/admissions")
async def admissions_page(request: Request):
    # <-- ADDED: Fetch the school info so the navbar and title work
    school = await SchoolInfo.find_one()

    categories = [
        "Creche (Day Care) - Ages 0-2",
        "Nursery - Ages 3-4",
        "Basic 1-6 - Ages 5-11",
    ]
    requirements = [
        "Birth Certificate",
        "Immunization Records",
        "2 Passport Photographs",
        "Transfer Certificate (for Basic classes)",
    ]

    return templates.TemplateResponse(
        request=request,
        name="admissions.html",
        # <-- ADDED: "school": school to the context
        context={
            "school": school,
            "categories": categories,
            "requirements": requirements,
        },
    )


@router.post("/admissions/enquire")
async def enquire(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    category: str = Form(...),
):
    # In a real app, save to DB or send email.
    # For now, redirect back to admissions with a success message
    return RedirectResponse(url="/admissions?success=true", status_code=303)
