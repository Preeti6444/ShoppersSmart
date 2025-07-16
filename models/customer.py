from sqlalchemy import Column, Integer, String
from main import Base 

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    location = Column(String)
    age = Column(Integer)
    gender = Column(String)