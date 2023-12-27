from fastapi import HTTPException,FastAPI, Depends, HTTPException, status
from dependencies import db_dependency,ItemBase,UserBase
from models.models import Item,User
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def check_is_username_available(user:UserBase,db:db_dependency):
    findUserWithGivenUsername = db.query(User).filter(User.name == user.name).first()
    if findUserWithGivenUsername is None:
        return True
    else:
        return False
    
def register(user:UserBase):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user.password=pwd_context.hash(user.password)
    print(user)
    if user is None:
        raise credentials_exception
    return user    
