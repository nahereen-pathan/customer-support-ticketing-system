from fastapi import APIRouter
from tasks import send_notification

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

notifications = []


@router.get("/")
def get_notifications():
    return notifications


@router.post("/")
def create_notification(message: str):

    notification = {
        "id": len(notifications) + 1,
        "message": message
    }

    notifications.append(notification)

    return {
        "message": "Notification Created",
        "data": notification
    }


@router.post("/notifications/send/{ticket_id}")
def trigger_notification(ticket_id: int):

    task = send_notification.delay(ticket_id)

    return {
        "task_id": task.id,
        "status": "Processing"
    }