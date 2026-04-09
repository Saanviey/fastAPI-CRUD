
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float , String


base = declarative_base()

class Product(base):

    __tablename__ ="product"
    
    id= Column( Integer ,primary_key= True , index=True )
    name = Column(String )
    description = Column(String)
    price= Column(Float)
    quantity= Column(Integer)

