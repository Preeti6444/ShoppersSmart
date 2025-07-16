from sqlalchemy import Column, Integer, String, Float, ForeignKey

def get_product_model(Base):
    class Product(Base):
        __tablename__ = 'products'
        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        category = Column(String(50))
        price = Column(Float)
        seller_id = Column(Integer, ForeignKey("customers.id"))
    return Product