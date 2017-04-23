

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float,ForeignKey

engine = create_engine(')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

# create the item model

class Item(Base):
    __tablename__="items"
    
    id=Column(Integer, primary_key=True)
    name=Column(String,nullable=False)
    description=Column(String)
    start_time=Column(DateTime,default=datetime.utcnow)
    
    #user = relationship("User",backref="user")
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    bid_item = relationship("Bid",backref = "bid_item2")
    
    

# create the user model

class User(Base):
    __tablename__="user"
    
    id=Column(Integer,primary_key=True)
    username=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    
    #item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    items = relationship("Item",backref="items2")
    bid = relationship("Bid", backref = "bid2")
    
# create the bid model

class Bid(Base):
    __tablename__="bid"
    
    id=Column(Integer,primary_key=True)
    price=Column(Float,nullable=False)
    bid_id = Column(Integer, ForeignKey("user.id"),nullable = False)
    item_id = Column(Integer,ForeignKey("items.id"),nullable = False)

# create the tables
Base.metadata.create_all(engine)












