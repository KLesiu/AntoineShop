from sqlalchemy import Column,Integer,String,Boolean
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

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(30))
    password = Column(String(255))
    admin = Column(Boolean)
    balance = Column(Integer)
    loyalityPoints = Column(Integer)
    email = Column(String(40))
    token = Column(String(40))
    verification = Column(Boolean)
    __allow_unmapped__ = True
    
