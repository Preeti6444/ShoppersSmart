from fastapi import FastAPI, HTTPException, Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from routes.customer_routes import router as customer_router
from models.customer import get_customer_model
from models.product import get_product_model
from models.transaction import get_transaction_model
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np

# Define Base
Base = declarative_base()

# FastAPI app
app = FastAPI()
app.include_router(customer_router)

# Database setup
DATABASE_URL = "sqlite:///shopper.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Models
Customer = get_customer_model(Base)
Product = get_product_model(Base)
Transaction = get_transaction_model(Base)

# Create Customer
@app.post("/customers/")
def create_customer(name: str, email: str):
    existing = session.query(Customer).filter(Customer.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    return {"message": "Customer created", "id": customer.id}

# Recommend Products
@app.get("/recommend/{customer_id}")
def recommend_products(customer_id: int = Path(..., title="Customer ID")):
    transactions = session.query(Transaction).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")

    data = [(t.customer_id, t.product_id) for t in transactions]
    df = pd.DataFrame(data, columns=["customer_id", "product_id"])
    matrix = df.pivot_table(index="customer_id", columns="product_id", aggfunc=lambda x: 1, fill_value=0)

    if customer_id not in matrix.index:
        raise HTTPException(status_code=404, detail="Customer has no transactions")

    knn = NearestNeighbors(metric="cosine", algorithm="brute")
    knn.fit(matrix)

    customer_vector = matrix.loc[customer_id].values.reshape(1, -1)
    distances, indices = knn.kneighbors(customer_vector, n_neighbors=3)

    neighbor_ids = matrix.index[indices.flatten()[1:]]
    neighbor_data = df[df.customer_id.isin(neighbor_ids)]

    user_products = set(df[df.customer_id == customer_id]["product_id"])
    neighbor_products = set(neighbor_data["product_id"])

    recommended_ids = list(neighbor_products - user_products)
    if not recommended_ids:
        return {"message": "No new products to recommend", "recommendations": []}

    recommended_products = session.query(Product).filter(Product.id.in_(recommended_ids)).all()
    return {
        "recommended_products": [
            {"id": p.id, "name": p.name, "category": p.category, "price": p.price}
            for p in recommended_products
        ]
    }