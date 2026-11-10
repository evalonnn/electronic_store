from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from .. import crud, schemas
from ..database import get_db
from ..dependencies import get_current_admin

router = APIRouter()


@router.post(
    "/products",
    response_model=schemas.ProductRead,
    dependencies=[Depends(get_current_admin)],
    status_code=201,
)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    if product.category_id is not None:
        category = crud.get_category(db, product.category_id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
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


@router.put(
    "/products/{product_id}",
    response_model=schemas.ProductRead,
    dependencies=[Depends(get_current_admin)],
)
def update_product(
    product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)
):
    if product.category_id is not None:
        category = crud.get_category(db, product.category_id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
    updated_product = crud.update_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete(
    "/products/{product_id}",
    response_model=schemas.ProductRead,
    dependencies=[Depends(get_current_admin)],
)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product
