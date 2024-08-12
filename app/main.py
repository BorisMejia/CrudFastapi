from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from . import models,schemas
from .Conexion import SessionLocal,engine
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

@app.get('/products/', response_model=List[schemas.ProductGet])
def show_product(db:Session=Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.post('/products/', response_model=schemas.ProductCreate)
def create_product(entrada:schemas.ProductCreate,db:Session=Depends(get_db)):
    new_product = models.Product(product_name=entrada.product_name,
                                     description = entrada.description,
                                    product_price=entrada.product_price, 
                                    quantity=entrada.quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put('/products/{product_id}', response_model=schemas.ProductUpdate)
def put_product(product_id:int, entrada:schemas.ProductUpdate,db:Session=Depends(get_db)):
    product = db.query(models.Product).filter_by(id=product_id)
    product= models.Product(product_name = entrada.product_name,description = entrada.description, product_price=entrada.product_price, quantity=entrada.quantity)
    db.commit
    db.refresh(product)
    return product

@app.delete('/products/{product_id}', response_model=schemas.Request)
def delete_product(product_id:int,  db:Session=Depends(get_db)):
    product = db.query(models.Product).filter_by(id=product_id)
    db.delete(product)
    db.commit
    request = schemas.Request(message="Producto eliminado correctamente")
    return 