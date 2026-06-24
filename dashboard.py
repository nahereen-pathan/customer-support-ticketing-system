from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Ticket, Customer, Agent

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard")
def get_dashboard(
    db: Session = Depends(get_db)
):
    return {
        "total_tickets": db.query(Ticket).count(),
        "total_customers": db.query(Customer).count(),
        "total_agents": db.query(Agent).count(),
        "open_tickets":
            db.query(Ticket)
            .filter(Ticket.status == "open")
            .count(),
        "closed_tickets":
            db.query(Ticket)
            .filter(Ticket.status == "closed")
            .count()
    }
