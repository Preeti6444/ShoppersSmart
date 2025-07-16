from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.product import Product
from main import get_db

router = APIRouter()

@router.post("/products/")
def create_product(product: dict, db: Session = Depends(get_db)):
    new_product = Product(**product)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}")
def update_product(product_id: int, update_data: dict, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in update_data.items():
        setattr(product, key, value)
    db.commit()
    return product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}