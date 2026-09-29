from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List

from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/products", response_model=schemas.ProductRead)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/products", response_model=List[schemas.ProductRead])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.get("/products/{product_id}", response_model=schemas.ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)

@router.put("/products/{product_id}", response_model=schemas.ProductRead)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db,product_id, product)

@router.delete("/products/{product_id}", response_model=schemas.ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(product_id, db)