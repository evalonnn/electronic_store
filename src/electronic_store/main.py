from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

from typing import List

import crud
import schemas

from database import get_db

app = FastAPI()

@app.post("/products", response_model=schemas.ProductRead)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products", response_model=List[schemas.ProductRead])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)

@app.put("/products/{product_id}", response_model=schemas.ProductRead)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db,product_id, product)

@app.delete("/products/{product_id}", response_model=schemas.ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(product_id, db)

@app.post("/categories", response_model=schemas.CategoryRead)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.get("/categories", response_model=List[schemas.CategoryRead])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)