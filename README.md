# ShoppersSmart
ShopperSmart - ML-Powered E-commerce Backend

ShopperSmart is a complete backend system for an e-commerce platform built using FastAPI, SQLite, and SQLAlchemy, with an integrated machine learning recommendation engine using K-Nearest Neighbors (KNN). This project allows for full CRUD operations on customers, products, and transactions, and offers personalized product recommendations.

# Table of Contents

Project Overview

Tech Stack

Project Structure

Features

Installation

Running the App

API Endpoints

ML Recommendation Engine

Testing the APIs

Deployment Guide

Screenshots

Credits

License

# Project Overview

ShopperSmart simulates a simplified version of an e-commerce backend system with features for customer management, product listings, purchase transactions, and product recommendations based on purchase patterns. The system is modular and designed for beginners learning backend + ML integration.

# Tech Stack

Python 3.9+

FastAPI - High-performance API framework

SQLite - Lightweight database

SQLAlchemy - ORM for database interactions

Pandas - Data manipulation

scikit-learn - Machine learning (KNN)

Uvicorn - ASGI server

# Project Structure

ShopperSmart/
├── main.py                      # Main FastAPI app & ML logic
├── models/
│   ├── customer.py            
│   ├── product.py              
│   └── transaction.py          
├── routes/
│   ├── customer_routes.py      
│   ├── product_routes.py       
│   └── transaction_routes.py   
├── README.md                   
└── requirements.txt            # Python dependencies

# Features

Create, Read, Update, Delete (CRUD) for customers, products, and transactions

Lightweight SQLite database

Modular code with routes and models

Machine Learning recommendations using collaborative filtering

Swagger UI auto-generated docs (/docs)

FastAPI async-ready architecture

# Installation

1. Clone the Repository

git clone https://github.com/Preeti6444/ShopperSmart.git
cd ShopperSmart

2. Create Virtual Environment (optional)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

requirements.txt sample:

fastapi
uvicorn
sqlalchemy
pandas
scikit-learn

# Running the App

Start your FastAPI server with Uvicorn:

uvicorn main:app --reload

Then go to:

http://127.0.0.1:8000/docs

Use the Swagger UI to interact with all endpoints easily.

# API Endpoints

Method

Endpoint

Description

GET

/customers/

List all customers

POST

/customers/

Create new customer

GET

/customers/{customer_id}

Get customer by ID

GET

/products/

List all products

POST

/products/

Add new product

GET

/products/{product_id}

Get product by ID

PUT

/products/{product_id}

Update product

DELETE

/products/{product_id}

Delete product

GET

/transactions/

List all transactions

POST

/transactions/

Create a new transaction

GET

/transactions/{transaction_id}

Get transaction by ID

PUT

/transactions/{transaction_id}

Update transaction

DELETE

/transactions/{transaction_id}

Delete transaction

GET

/recommend/{customer_id}

# Recommend products using KNN

# ML Recommendation Engine

# Algorithm: K-Nearest Neighbors (KNN)

Uses historical transaction data to build a customer-product matrix

Finds similar customers using cosine similarity

Recommends products bought by similar users

Excludes products the user already purchased

# Libraries Used

pandas for matrix creation

sklearn.neighbors.NearestNeighbors for similarity

Example Response:

{
  "recommended_products": [
    {
      "id": 3,
      "name": "Shoes",
      "category": "Footwear",
      "price": 3200
    }
  ]
}

# Testing the APIs

You can use:

Swagger UI: http://127.0.0.1:8000/docs

Postman: Import openapi.json

To add data:

Create customers

Add products

Create transactions

Call /recommend/{customer_id}

# Deployment Guide

You can deploy to:

PythonAnywhere (Beginner-friendly)

Render.com (Free hosting for FastAPI)

Docker + VPS

Deploy on Render (example):

Push code to GitHub

Create new Web Service on Render

Set build command: pip install -r requirements.txt

Set start command: uvicorn main:app --host 0.0.0.0 --port 10000

Expose port 10000

📸 Screenshots

# Add screenshots of:

Swagger UI

Sample recommendation response

Terminal showing running server & routes

# Credits

Project by Preeti Vaychal

GitHub: 

LinkedIn: 