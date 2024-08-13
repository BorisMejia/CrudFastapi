from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..models import Category_models
from ..schemas import Category
from ..Conexion import get_db

router = APIRouter()

@router.get('/categories/', response_model=List[Category.CategoryGet])
def show_category(db: Session = Depends(get_db)):
    categories = db.query(Category_models.Category).all()
    return categories

@router.post('/categories/', response_model=Category.CategoryCreate)
def create_category(entrada: Category.CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category_models.Category(category_name=entrada.category_name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.put('/categories/{category_id}', response_model=Category.CategoryUpdate)
def update_category(category_id: int, entrada: Category.CategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(Category_models.Category).filter_by(category_id=category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category.category_name = entrada.category_name
    db.commit()
    db.refresh(category)
    return category

@router.delete('/categories/{category_id}', response_model=Category.Request)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category_models.Category).filter(Category_models.Category.category_id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    request = Category.Request(message="Categoria eliminada correctamente")
    return request
