from pydantic import BaseModel
from typing import Optional

class ProductGet(BaseModel):
    product_id:int
    product_name:str
    description:str
    product_price:int
    quantity:int

    class config:
        orm_mode = True

class ProductCreate(BaseModel):
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


