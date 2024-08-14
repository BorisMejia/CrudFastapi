from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..Conexion import Base

class Category(Base):
    __tablename__ = 'category'
    
    category_id = Column(Integer, primary_key=True, index=True, )
    category_name = Column(String(50), unique=True, index=True)

    products = relationship("Product", back_populates="category")
