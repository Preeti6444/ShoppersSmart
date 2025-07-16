from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime

def get_transaction_model(Base):
    class Transaction(Base):
        __tablename__ = 'transactions'
        id = Column(Integer, primary_key=True)
        customer_id = Column(Integer, ForeignKey("customers.id"))
        product_id = Column(Integer, ForeignKey("products.id"))
        timestamp = Column(DateTime, default=datetime.utcnow)
    return Transaction