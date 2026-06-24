from fastapi import APIRouter

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/summary")
def get_summary():
    return {
        "total_customers": 50,
        "total_agents": 5,
        "total_tickets": 120,
        "open_tickets": 25,
        "closed_tickets": 95
    }

