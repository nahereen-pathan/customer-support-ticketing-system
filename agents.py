from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Agent
from schemas import AgentCreate

router = APIRouter(tags=["Agents"])


@router.post("/agents")
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db)
):
    new_agent = Agent(
        name=agent.name,
        email=agent.email,
        department=agent.department
    )

    db.add(new_agent)
    db.commit()

    return {
        "message": "Agent created successfully"
    }


@router.get("/agents")
def get_agents(
    db: Session = Depends(get_db)
):
    return db.query(Agent).all()