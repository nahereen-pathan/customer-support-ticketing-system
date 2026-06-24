from fastapi import APIRouter

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

roles = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "Agent"},
    {"id": 3, "name": "Customer"}
]


@router.get("/")
def get_roles():
    return roles