from fastapi import HTTPException
from dependencies import db_dependency,ItemBase,UserBase,UserLogin
from models.models import Item,User
from helpers.helpers import check_is_username_available,hash_user_password,check_user_password
from helpers.mailer import send_verification_email
import secrets

async def create_item_service(item: ItemBase, db: db_dependency):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    return item

async def read_item_service(item_id:int,db:db_dependency):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="Item not found")
    return item
        

async def delete_item_service(item_id:int,db:db_dependency):
    item = db.query(Item).filter(Item.id==item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="Item not found")
    else:
        db.delete(item)
        db.commit()
        return item
    
async def create_user_service(user:UserBase,db:db_dependency):
    if await check_is_username_available(user,db) == False:
        raise HTTPException(status_code=409,detail="This username is not available")
    user = hash_user_password(user)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    verification_token = secrets.token_urlsafe(16)
    send_verification_email(user.email,verification_token)
    return user

async def read_user_service(user_id:int,db:db_dependency):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

async def delete_user_service(user_id:int,db:db_dependency):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    else:
        db.delete(user)
        db.commit()
        return user
async def user_login_service(user:UserLogin,db:db_dependency):
    findUser = db.query(User).filter(User.name == user.name).first()
    if findUser is None:
        raise HTTPException(status_code=404,detail="User not found")
    else:
        result = check_user_password(findUser.password,user.password)
        if result:
            return findUser
        else:
            raise HTTPException(status_code=401,detail="Wrong password")