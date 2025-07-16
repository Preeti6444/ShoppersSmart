from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define shared Base
Base = declarative_base()

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

import models.customer
import models.product
import models.transaction

# Create tables
Base.metadata.create_all(bind=engine)

print("All tables created successfully!")