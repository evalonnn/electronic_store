from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from .. import crud, schemas
from ..database import get_db

router = APIRouter()


@router.post("/register", response_model=schemas.UserRead, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user is not None:
        raise HTTPException(status_code=409, detail="Username already registered")

    existing_email = crud.get_user_by_email(db, user.email)
    if existing_email is not None:
        raise HTTPException(status_code=409, detail="Email already registered")

    return crud.create_user(db, user)
