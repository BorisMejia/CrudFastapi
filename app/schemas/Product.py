from pydantic import BaseModel, Field
from .Category import CategoryGet


class ProductGet(BaseModel):
    product_id: int = Field
    product_name: str = Field
    description: str = Field
    product_price: int = Field
    quantity: int = Field
    category: CategoryGet = Field

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    product_name: str = Field
    description: str = Field
    product_price: int = Field
    quantity: int = Field
    category_id: int = Field

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    product_name: str = Field
    description: str = Field
    product_price: int = Field
    quantity: int = Field
    category_id: int = Field

    class Config:
        from_attributes = True

class Request(BaseModel):
    message:str


