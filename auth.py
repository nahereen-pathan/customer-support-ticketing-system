from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserLogin
from passlib.context import CryptContext
from security import create_access_token

router = APIRouter(tags=["Authentication"])
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    
    new_user = User(
        name=user.name,
        email=user.email,
        password=pwd_context.hash(user.password)
    )

    db.add(new_user)
    db.commit()

    return{
        "message" : " User Registered Successfully"
    }


@router.post("/login")
def login(
        user : UserLogin,
        db : Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    if not pwd_context.verify(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    token = create_access_token(
    {
        "user_id": db_user.id,
        "role": db_user.role
    }
)

    return {
        "access_token": token,
        "role": db_user.role,
        "message": "Login Successful"
}

