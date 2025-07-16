from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.transaction import Transaction
from main import get_db
from datetime import datetime

router = APIRouter()

@router.post("/transactions/")
def create_transaction(transaction: dict, db: Session = Depends(get_db)):
    new_transaction = Transaction(**transaction, purchase_date=datetime.utcnow())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@router.get("/transactions/")
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

@router.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.put("/transactions/{transaction_id}")
def update_transaction(transaction_id: int, update_data: dict, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    for key, value in update_data.items():
        setattr(transaction, key, value)
    db.commit()
    return transaction

@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()
    return {"message": "Transaction deleted successfully"}