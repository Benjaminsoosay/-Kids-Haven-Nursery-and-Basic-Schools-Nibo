from app.models.school_info import SchoolInfo
from app.models.staff import Staff


async def get_homepage_data():
    # Fetch the school info document
    school = await SchoolInfo.find_one()

    # Fetch all staff documents
    staff_members = await Staff.find_all().to_list()

    # Return them together
    return {"school": school, "staff_members": staff_members}
