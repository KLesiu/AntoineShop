from fastapi import APIRouter,HTTPException,status
from dependencies import db_dependency,ItemBase,UserBase
from models.models import Item,User

router = APIRouter()


# Items
@router.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemBase, db: db_dependency):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()


@router.get("/items/{item_id}",status_code=status.HTTP_200_OK)
async def read_item(item_id:int,db:db_dependency):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="Item not found")
    return item


@router.delete("/items/{item_id}",status_code=status.HTTP_202_ACCEPTED)
async def delete_item(item_id:int,db:db_dependency):
    item = db.query(Item).filter(Item.id==item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="Item not found")
    else:
        db.delete(item)
        db.commit()
        return item

# Users
@router.post("/users/",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase,db:db_dependency):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()


@router.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def read_user(user_id:int,db:db_dependency):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@router.delete("/users/{user_id}",status_code=status.HTTP_202_ACCEPTED)
async def delete_user(user_id:int,db:db_dependency):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    else:
        db.delete(user)
        db.commit()
        return user



    