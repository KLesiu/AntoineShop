from fastapi import APIRouter,HTTPException,status
from dependencies import db_dependency,ItemBase,UserBase
from models.models import Item,User

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
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
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