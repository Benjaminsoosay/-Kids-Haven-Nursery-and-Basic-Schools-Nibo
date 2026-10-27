from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models.school_info import SchoolInfo
from app.models.staff import Staff  # <-- NEW: Import the Staff model

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home_page(request: Request):
    # 1. Fetch the school info from MongoDB
    school = await SchoolInfo.find_one()

    # 2. Fetch all staff members from MongoDB (NEW)
    staff_members = await Staff.find_all().to_list()

    # 3. Pass BOTH pieces of data to the HTML template (UPDATED)
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"school": school, "staff_members": staff_members},
    )
