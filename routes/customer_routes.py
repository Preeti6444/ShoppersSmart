from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from models.customer import get_customer_model

# Database setup
DATABASE_URL = "sqlite:///shopper.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Load model
Customer = get_customer_model(Base)

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router
router = APIRouter()

# Now includes POST route too
@router.post("/customers/")
def create_customer(name: str, email: str, db: Session = Depends(get_db)):
    existing = db.query(Customer).filter(Customer.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    customer = Customer(name=name, email=email)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return {"message": "Customer created", "id": customer.id}

@router.get("/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer