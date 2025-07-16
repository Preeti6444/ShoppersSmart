from sqlalchemy import Column, Integer, String

def get_customer_model(Base):
    class Customer(Base):
        __tablename__ = 'customers'
        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        email = Column(String(100), unique=True)
    return Customer