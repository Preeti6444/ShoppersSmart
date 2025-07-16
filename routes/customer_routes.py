from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.customer import Customer
from main import get_db

router = APIRouter()

@router.post("/customers/")
def create_customer(customer: dict, db: Session = Depends(get_db)):
    new_customer = Customer(**customer)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@router.get("/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, update_data: dict, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in update_data.items():
        setattr(customer, key, value)
    db.commit()
    return customer

@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}