from fastapi import Depends
from pydantic import BaseModel
from typing import Annotated
from database import engine, SessionLocal,Base
from sqlalchemy.orm import Session


class ItemBase(BaseModel):
    name: str
    price: int
    brand: str
    size: str
    condition: str
    views: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]