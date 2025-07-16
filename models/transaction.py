from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from main import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    purchase_date = Column(DateTime, default=datetime.utcnow)