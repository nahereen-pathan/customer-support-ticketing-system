from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Customer
from schemas import CustomerCreate

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    new_customer = Customer(**customer.dict())

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer