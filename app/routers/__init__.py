# This makes the routers easily accessible
# e.g., from app.routers import home, about
from . import home
from . import about
from . import admissions
from . import contact
from . import gallery

__all__ = ["home", "about", "admissions", "contact", "gallery"]
