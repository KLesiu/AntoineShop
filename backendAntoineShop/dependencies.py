from fastapi import Depends
from pydantic import BaseModel
from typing import Annotated
from database import engine, SessionLocal,Base
from sqlalchemy.orm import Session

class Token(BaseModel):
    access_token:str
    token_type:str

class ItemBase(BaseModel):
    name: str
    price: int
    brand: str
    size: str
    condition: str
    views: int

class UserBase(BaseModel):
    name:str
    password:str
    admin:bool
    balance:int
    loyalityPoints:int
    email:str
    token: str
    verification: bool
    

class UserLogin(BaseModel):
    name:str
    password:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]