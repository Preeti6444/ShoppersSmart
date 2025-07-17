from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from models.customer import get_customer_model

DATABASE_URL = "sqlite:///shopper.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

Customer = get_customer_model(Base)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer