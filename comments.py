from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Comment
from schemas import CommentCreate

router = APIRouter(tags=["Comments"])


@router.post("/comments")
def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db)
):
    new_comment = Comment(
        ticket_id=comment.ticket_id,
        message=comment.message
    )

    db.add(new_comment)
    db.commit()

    return {
        "message": "Comment Added Successfully"
    }


@router.get("/comments")
def get_comments(
    db: Session = Depends(get_db)
):
    return db.query(Comment).all()