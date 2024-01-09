from fastapi import HTTPException
from dependencies import db_dependency,ItemBase,UserBase,UserLogin
from models.models import Item,User
from helpers.helpers import check_is_username_available,hash_user_password,check_user_password,verify_user_token,update_user_balance
from helpers.mailer import send_verification_email,send_email_after_purchase
import secrets

async def create_item_service(item: ItemBase, db: db_dependency):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    return item

async def get_items_service(db:db_dependency):
    items = db.query(Item).all()
    if items is None:
        raise HTTPException(status_code=404,detail="Items not found")
    return items

async def read_item_service(item_id:int,db:db_dependency):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="Item not found")
    return item

async def edit_item_service(item_id:int,db:db_dependency,item:ItemBase):
    findItem = db.query(Item).filter(Item.id == item_id).first()
    if findItem is None:
        raise HTTPException(status_code=404,detail="Item not found")
    else:
       findItem.brand = item.brand
       findItem.condition = item.condition
       findItem.name = item.name
       findItem.price = item.price
       findItem.size = item.size
       db.commit()
       db.refresh(findItem)
       return findItem        

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
    verification_token = secrets.token_urlsafe(16)
    user.token = verification_token
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()

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
            return {
                'name': findUser.name,
                'admin': findUser.admin,
                'balance': findUser.balance,
                'id': findUser.id,
                'loyalityPoints': findUser.loyalityPoints,
                'verification': findUser.verification
            }
        else:
            raise HTTPException(status_code=401,detail="Wrong password")
        
def user_verification_service(db:db_dependency,token):
    isVerified = verify_user_token(token,db)
    if isVerified:
        findUser = db.query(User).filter(User.token == token).first()
        findUser.verification = True
        db.commit()
        db.refresh(findUser)
        return "You are verified"
    else:
        return "Incorrect token!"

async def user_balance_service(db:db_dependency,user_id:int,credits:int):
    user = db.query(User).filter(User.id == user_id).first()
    return update_user_balance(user,db,credits)

async def user_email_after_purchase_service(db:db_dependency,user_id:int,price:int,items,address:str):
    user = db.query(User).filter(User.id == user_id).first()
    if(user.balance < price):
        return "You dont have enough credits to buy this items, please add credits then try again"
    return send_email_after_purchase(user.email,price,items,address)
