from fastapi import HTTPException,FastAPI, Depends, HTTPException, status
from dependencies import db_dependency,ItemBase,UserBase,UserLogin
from models.models import Item,User
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def check_is_username_available(user:UserBase,db:db_dependency):
    findUserWithGivenUsername = db.query(User).filter(User.name == user.name).first()
    if findUserWithGivenUsername is None:
        return True
    else:
        return False
    
def hash_user_password(user:UserBase):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user.password=pwd_context.hash(user.password)
    if user is None:
        raise credentials_exception
    return user

def check_user_password(correctPassword,password):
    result = bcrypt.checkpw(password.encode('utf-8'),correctPassword.encode('utf-8'))
    return result

def verify_user_token(token,db:db_dependency):
    findUserWithGivenToken = db.query(User).filter(User.token == token).first()
    if findUserWithGivenToken is None:
        return False
    else:
        return True

def update_user_balance(user:UserBase,db:db_dependency,credits:int):
    user.balance += credits
    if(user.balance < 0):
        return "You dont have enough money"
    db.commit()
    db.refresh(user)
    return user.balance


    



