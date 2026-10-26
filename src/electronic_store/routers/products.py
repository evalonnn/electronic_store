from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
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
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/products/{product_id}", response_model=schemas.ProductRead)
def update_product(
    product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)
):
    update_product = crud.update_product(db, product_id, product)
    if update_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return update_product


@router.delete("/products/{product_id}", response_model=schemas.ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    delete_product = crud.delete_product(db, product_id)
    if delete_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return delete_product
