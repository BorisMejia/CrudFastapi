from pydantic import BaseModel
from typing import Optional, List


class CategoryGet(BaseModel):
    category_id: int
    category_name: str
    

    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    category_name: str

    class Config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    category_name: Optional[str] = None

    class Config:
        from_attributes = True

class Request(BaseModel):
    message:str
