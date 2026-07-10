from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

# Import models so SQLAlchemy registers them
import app.models

app = FastAPI(title="RentMate AI API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "RentMate AI Backend Running"}