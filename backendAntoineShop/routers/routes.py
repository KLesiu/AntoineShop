from fastapi import APIRouter,status
from dependencies import db_dependency,ItemBase,UserBase,UserLogin

from services.services import create_item_service,create_user_service,delete_item_service,delete_user_service,read_item_service,read_user_service,user_login_service,user_verification_service,edit_item_service,get_items_service

router = APIRouter()




# Items
@router.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemBase, db: db_dependency):
    return await create_item_service(item,db)

@router.get("/items/",status_code=status.HTTP_200_OK)
async def get_items(db:db_dependency):
    return await get_items_service(db)

@router.get("/items/{item_id}",status_code=status.HTTP_200_OK)
async def read_item(item_id:int,db:db_dependency):
    return await read_item_service(item_id,db)
   
@router.patch('/items/{item_id}',status_code=status.HTTP_200_OK)
async def edit_item(item_id:int,db:db_dependency,item:ItemBase):
    return await edit_item_service(item_id,db,item)

@router.delete("/items/{item_id}",status_code=status.HTTP_202_ACCEPTED)
async def delete_item(item_id:int,db:db_dependency):
    return await delete_item_service(item_id,db)

# Users
@router.post("/users/",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase,db:db_dependency):
    return await create_user_service(user,db)

@router.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def read_user(user_id:int,db:db_dependency):
    return await read_user_service(user_id,db)

@router.delete("/users/{user_id}",status_code=status.HTTP_202_ACCEPTED)
async def delete_user(user_id:int,db:db_dependency):
    return await delete_user_service(user_id,db)

@router.post("/users/login",status_code=status.HTTP_200_OK)
async def login_user(user:UserLogin,db:db_dependency):
    return await user_login_service(user,db)

@router.post("/users/verify",status_code=status.HTTP_200_OK)
async def verify_user(db:db_dependency,token):
    return await user_verification_service(db,token)


    