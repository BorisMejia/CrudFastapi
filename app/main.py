from fastapi import FastAPI
from starlette.responses import RedirectResponse
from .models import Product_models, Category_models
from .routers import product_routers, category_routers
from .Conexion import engine

from sqlalchemy.exc import SQLAlchemyError



#Crear DB
"""

Product_models.Base.metadata.create_all(bind=engine)
Category_models.Base.metadata.create_all(bind=engine)
#"""
#Reset DB
#"""
def reset_database():
    try:
            Product_models.Base.metadata.drop_all(bind=engine)  # Elimina todas las tablas
            Category_models.Base.metadata.drop_all(bind=engine)
            Product_models.Base.metadata.create_all(bind=engine)  # Vuelve a crear las tablas
            Category_models.Base.metadata.create_all(bind=engine)  # Vuelve a crear las tablas
    except SQLAlchemyError as e:
        print(f"Error al reiniciar la base de datos: {e}")

reset_database()
#"""

app = FastAPI()

app.include_router(product_routers.router)
app.include_router(category_routers.router)

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

