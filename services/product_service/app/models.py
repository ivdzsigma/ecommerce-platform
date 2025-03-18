# services/product_service/app/models.py
from sqlalchemy import Column, Integer, String, Float, ARRAY
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    tags = Column(ARRAY(String))
    images = Column(ARRAY(String))