from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.models.gallery import GalleryImage
from app.models.staff import Staff
from app.models.contact import ContactMessage
from app.models.school_info import SchoolInfo
from bson import ObjectId
import secrets

router = APIRouter(prefix="/admin", tags=["Admin Dashboard"])
templates = Jinja2Templates(directory="templates")
security = HTTPBasic()


# --- Simple Security ---
def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "kids2026")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True


# --- Dashboard Views ---
@router.get("")
async def admin_dashboard(request: Request, auth: bool = Depends(verify_admin)):
    school = await SchoolInfo.find_one()
    image_count = await GalleryImage.count()
    staff_count = await Staff.count()
    message_count = await ContactMessage.count()

    return templates.TemplateResponse(
        request=request,
        name="admin/dashboard.html",
        context={
            "school": school,
            "image_count": image_count,
            "staff_count": staff_count,
            "message_count": message_count,
        },
    )


# --- Manage Gallery ---
@router.get("/gallery")
async def admin_gallery(request: Request, auth: bool = Depends(verify_admin)):
    images = await GalleryImage.find_all().to_list()
    school = await SchoolInfo.find_one()
    return templates.TemplateResponse(
        request=request,
        name="admin/gallery.html",
        context={"school": school, "images": images},
    )


@router.post("/gallery/add")
async def add_image(
    title: str = Form(...),
    description: str = Form(...),
    image_url: str = Form(...),
    category: str = Form(...),
    auth: bool = Depends(verify_admin),
):
    new_image = GalleryImage(
        title=title, description=description, image_url=image_url, category=category
    )
    await new_image.insert()
    return RedirectResponse(url="/admin/gallery", status_code=303)


@router.post("/gallery/delete/{image_id}")
async def delete_image(image_id: str, auth: bool = Depends(verify_admin)):
    image = await GalleryImage.get(ObjectId(image_id))
    if image:
        await image.delete()
    return RedirectResponse(url="/admin/gallery", status_code=303)
