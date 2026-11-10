from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List

from .. import crud, schemas
from ..database import get_db
from ..dependencies import get_current_admin

router = APIRouter()


@router.post(
    "/categories",
    response_model=schemas.CategoryRead,
    dependencies=[Depends(get_current_admin)],
    status_code=201,
)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.get("/categories", response_model=List[schemas.CategoryRead])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)
