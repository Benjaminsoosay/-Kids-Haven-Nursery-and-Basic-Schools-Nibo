from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import bcrypt  # <-- Using bcrypt directly instead of passlib
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])
templates = Jinja2Templates(directory="templates")


# Modern Bcrypt functions
def get_password_hash(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


# --- Register ---
@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/register.html")


@router.post("/register")
async def register_user(
    request: Request,
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    try:
        # Check if user already exists
        existing_user = await User.find_one(User.email == email)
        if existing_user:
            return templates.TemplateResponse(
                request=request,
                name="auth/register.html",
                context={"error": "Email already registered."},
            )

        # Create new user (Hash the password)
        hashed_pw = get_password_hash(password)
        new_user = User(full_name=full_name, email=email, password_hash=hashed_pw)
        await new_user.insert()

        # Log them in immediately
        request.session["user_id"] = str(new_user.id)
        request.session["user_name"] = new_user.full_name

        return RedirectResponse(url="/auth/dashboard", status_code=303)
    except Exception as e:
        # If it fails, print the exact error to the terminal
        print(f"🔴 REGISTRATION ERROR: {e}")
        return templates.TemplateResponse(
            request=request,
            name="auth/register.html",
            context={"error": "An error occurred. Please try again."},
        )


# --- Login ---
@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/login.html")


@router.post("/login")
async def login_user(
    request: Request, email: str = Form(...), password: str = Form(...)
):
    user = await User.find_one(User.email == email)
    if not user or not verify_password(password, user.password_hash):
        return templates.TemplateResponse(
            request=request,
            name="auth/login.html",
            context={"error": "Invalid email or password."},
        )

    # Save user to session
    request.session["user_id"] = str(user.id)
    request.session["user_name"] = user.full_name

    return RedirectResponse(url="/auth/dashboard", status_code=303)


# --- Dashboard ---
@router.get("/dashboard")
async def parent_dashboard(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/auth/login", status_code=303)

    user = await User.get(user_id)
    return templates.TemplateResponse(
        request=request, name="auth/dashboard.html", context={"user": user}
    )


# --- Logout ---
@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")
