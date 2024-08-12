from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_id:Optional[int]
    product_name:str
    description:str
    product_price:int
    quantity:int

    class config:
        orm_mode = True

class ProductUpdate(BaseModel):
    product_name:str
    description:str
    product_price:int
    quantity:int

    class config:
        orm_mode = True

class Request(BaseModel):
    message:str


