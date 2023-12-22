from sqlalchemy import Column,Integer,String
from database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    price = Column(Integer)
    brand = Column(String(20))
    size = Column(String(5))
    condition = Column(String(10))
    views = Column(Integer)
    
