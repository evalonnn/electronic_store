from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(ge=0)
    stock: int = Field(ge=0)
    category_id: int | None = None

class ProductRead(ProductCreate):
    id: int

class CategoryCreate(BaseModel):
    name: str

class CategoryRead(CategoryCreate):
    id: int 


    