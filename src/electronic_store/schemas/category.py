from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryRead(CategoryCreate):
    id: int 
