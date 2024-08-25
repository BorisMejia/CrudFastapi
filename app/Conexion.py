from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "5432"
DATABASE_NAME = "fastapi"
DATABASE_USER = "root"
DATABASE_PASSWORD = "root"

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

#DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/fastapi"
#DATABASE_URL = "postgresql://root:root@postgresql:5432/fastapi"
engine = create_engine(DATABASE_URL)
#SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

Base = declarative_base()