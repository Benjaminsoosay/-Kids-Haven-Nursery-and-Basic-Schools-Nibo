from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models.school_info import SchoolInfo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/about")
async def about_page(request: Request):
    school = await SchoolInfo.find_one()
    return templates.TemplateResponse(
        request=request, name="about.html", context={"school": school}
    )
