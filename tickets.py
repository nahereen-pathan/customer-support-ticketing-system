from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Ticket
from schemas import(
    TicketCreate,
    TicketUpdate
)

router = APIRouter(tags=["Tickets"])
@router.post("/tickets")
def create_ticket(ticket:TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description
    )

    db.add(new_ticket)
    db.commit()
    return{
        "message": "Ticket created Successfully"
    }

@router.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@router.put("tickets/{ticket_id}")
def update_ticket(ticket_id:int, ticket:TicketUpdate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    db_ticket.status = ticket.status
    db.commit()
    return{
        "message":"Ticket Updated successfully"
    }