from fastapi import APIRouter, Depends, HTTPException, status
from ..database.connection import get_db
from ..database import model
from ..schemas.request import User
from ..schemas.response import ShowUser
from ..utils.hash import Hash
from sqlalchemy.orm import Session


router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = model.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user
