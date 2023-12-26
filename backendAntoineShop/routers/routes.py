from fastapi import APIRouter,status
from dependencies import db_dependency,ItemBase,UserBase

from services.services import create_item_service,create_user_service,delete_item_service,delete_user_service,read_item_service,read_user_service

router = APIRouter()


# Items
@router.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemBase, db: db_dependency):
    return await create_item_service(item,db)



@router.get("/items/{item_id}",status_code=status.HTTP_200_OK)
async def read_item(item_id:int,db:db_dependency):
    return await read_item_service(item_id,db)
   


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



    