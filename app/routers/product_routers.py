"""from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session
from typing import List
from ..models import Product_models, Category_models
from ..schemas import Product
from ..Conexion import get_db


router = APIRouter()


@router.get('/products/', response_model=List[Product.ProductGet])
def show_product(db:Session=Depends(get_db)):
    products = db.query(Product_models.Product).all()
    return products

@router.post('/products/', response_model=Product.ProductCreate)
def create_product(entrada:Product.ProductCreate,db:Session=Depends(get_db)):
    new_product = Product_models.Product(product_name=entrada.product_name,
                                     description = entrada.description,
                                    product_price=entrada.product_price, 
                                    quantity=entrada.quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.put('/products/{product_id}', response_model=Product.ProductUpdate)
def update_product(product_id: int, entrada:Product.ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product_models.Product).filter_by(product_id=product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.product_name = entrada.product_name
    product.description = entrada.description
    product.product_price = entrada.product_price
    product.quantity = entrada.quantity

    db.commit()
    db.refresh(product)
    return product

@router.delete('/products/{product_id}', response_model=Product.Request)
def delete_product(product_id:int,  db:Session=Depends(get_db)):
    product = db.query(Product_models.Product).filter(Product_models.Product.product_id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(product)
    db.commit()
    request = Product.Request(message="Producto eliminado correctamente")
    return request"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..models import Product_models
from ..schemas import Product
from ..Conexion import get_db

router = APIRouter() 

@router.get('/products/', response_model=List[Product.ProductGet])
def show_product(db: Session = Depends(get_db)):
    products = db.query(Product_models.Product).all()
    return products

@router.post('/products/', response_model=Product.ProductCreate) 
def create_product(entrada: Product.ProductCreate, db: Session = Depends(get_db)):
    new_product = Product_models.Product(
        product_name=entrada.product_name,
        description=entrada.description,
        product_price=entrada.product_price,
        quantity=entrada.quantity,
        category_id=entrada.category_id  
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.put('/products/{product_id}', response_model=Product.ProductUpdate)  
def update_product(product_id: int, entrada: Product.ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product_models.Product).filter_by(product_id=product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if entrada.product_name is not None:
        product.product_name = entrada.product_name
    if entrada.description is not None:
        product.description = entrada.description
    if entrada.product_price is not None:
        product.product_price = entrada.product_price
    if entrada.quantity is not None:
        product.quantity = entrada.quantity
    if entrada.category_id is not None:
        product.category_id = entrada.category_id

    db.commit()
    db.refresh(product)
    return product

@router.delete('/products/{product_id}', response_model=Product.Request)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product_models.Product).filter(Product_models.Product.product_id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    request = Product.Request(message="Producto eliminado correctamente")
    return request
