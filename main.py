from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define Base here
Base = declarative_base()

from models.customer import get_customer_model
from models.product import get_product_model
from models.transaction import get_transaction_model

Customer = get_customer_model(Base)
Product = get_product_model(Base)
Transaction = get_transaction_model(Base)

# DB setup
DATABASE_URL = "sqlite:///shopper.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

app = FastAPI()

@app.post("/customers/")
def create_customer(name: str, email: str):
    existing = session.query(Customer).filter(Customer.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    return {"message": "Customer created", "id": customer.id}