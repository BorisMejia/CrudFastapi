from pydantic import BaseModel, Field

class CategoryGet(BaseModel):
    category_id: int = Field
    category_name: str = Field
    

    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    category_name: str = Field

    class Config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    category_name: str = Field

    class Config:
        from_attributes = True

class Request(BaseModel):
    message:str
