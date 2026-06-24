from celery_worker import celery_app
import time

@celery_app.task
def send_notification(ticket_id: int):

    print(f"Processing Ticket {ticket_id}", flush=True)

    time.sleep(5)

    print("Notification Sent Successfully", flush=True)

    return {
        "message": f"Notification sent for Ticket {ticket_id}"
    }