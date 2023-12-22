from fastapi import APIRouter,HTTPException,status
from dependencies import db_dependency,ItemBase
from models.models import Item

router = APIRouter()

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