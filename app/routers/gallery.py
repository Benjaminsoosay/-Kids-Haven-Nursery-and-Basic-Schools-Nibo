from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models.gallery import GalleryImage
from app.models.school_info import SchoolInfo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/gallery")
async def gallery_page(request: Request, category: str = "All"):
    # Fetch school info so the navbar and title work
    school = await SchoolInfo.find_one()

    # Fetch all images or filter by category
    if category == "All":
        images = await GalleryImage.find_all().to_list()
    else:
        # FIXED: Changed 'category=category' to 'GalleryImage.category == category'
        images = await GalleryImage.find(GalleryImage.category == category).to_list()

    categories = ["All", "Classrooms", "Playground", "Events", "Learning Activities"]

    return templates.TemplateResponse(
        request=request,
        name="gallery.html",
        context={
            "school": school,
            "images": images,
            "categories": categories,
            "selected_category": category,
        },
    )
