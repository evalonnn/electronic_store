from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .. import crud, schemas
from ..database import get_db
from ..security import create_access_token
from ..dependencies import get_current_user

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


@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            headers={"WWW-Authenticate": "Bearer"},
            status_code=401,
            detail="Incorrect username or password",
        )

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=schemas.UserRead)
def me(current_user=Depends(get_current_user)):
    return current_user
