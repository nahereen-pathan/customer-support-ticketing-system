from fastapi import APIRouter

router = APIRouter(
    prefix="/activity-logs",
    tags=["Activity Logs"]
)

activity_logs = []


@router.get("/")
def get_logs():
    return activity_logs


@router.post("/")
def create_log(action: str, user: str):

    log = {
        "id": len(activity_logs) + 1,
        "action": action,
        "user": user
    }

    activity_logs.append(log)

    return {
        "message": "Log Created Successfully",
        "data": log
    }

