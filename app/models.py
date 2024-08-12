from sqlalchemy import Column, Integer, String, ForeignKey
from .Conexion import Base

class Product(Base):
    __tablename__  ='product'
    product_id = Column(Integer,primary_key=True,index=True)
    product_name = Column(String(25))
    description = Column(String(30))
    product_price = Column(Integer)
    quantity = Column(Integer)

    """category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="products") """
