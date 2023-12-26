from fastapi import HTTPException
from dependencies import db_dependency,ItemBase,UserBase
from models.models import Item,User


async def check_is_username_available(user:UserBase,db:db_dependency):
    findUserWithGivenUsername = db.query(User).filter(User.name == user.name).first()
    if findUserWithGivenUsername is None:
        return True
    else:
        return False
