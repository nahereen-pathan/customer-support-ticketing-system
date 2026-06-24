from fastapi import FastAPI

from database import Base, engine

from models import User, Ticket



from auth import router as auth_router
from tickets import router as ticket_router
from customers import router as customer_router
from models import User, Ticket, Customer, Agent
from agents import router as agent_router
from dashboard import router as dashboard_router
from comments import router as comment_router
from roles import router as role_router
from activity_logs import router as activity_router
from attachments import router as attachment_router
from notifications import router as notification_router
from reports import router as report_router
from fastapi.staticfiles import StaticFiles



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer Support Ticketing System"
)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(auth_router)
app.include_router(ticket_router)
app.include_router(customer_router)
app.include_router(agent_router)
app.include_router(dashboard_router)
app.include_router(comment_router)
app.include_router(activity_router)
app.include_router(notification_router)
app.include_router(report_router)
app.include_router(attachment_router)


@app.get("/")
def root():
    return {
        "message": "Ticketing System Running"
    }

