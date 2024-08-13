from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING


from .Category import CategoryGet


class ProductGet(BaseModel):
    product_id: int
    product_name: str
    description: str
    product_price: int
    quantity: int
    category: Optional[CategoryGet] = None

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    product_name: str
    description: str
    product_price: int
    quantity: int
    category_id: Optional[int] = None

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    description: Optional[str] = None
    product_price: Optional[int] = None
    quantity: Optional[int] = None
    category_id: Optional[int] = None

    class Config:
        from_attributes = True

class Request(BaseModel):
    message:str


