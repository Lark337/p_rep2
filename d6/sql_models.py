from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)
    email = Column(String)
    password = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer,ForeignKey('users.id'))
    product_id = Column(Integer,ForeignKey('products.id'))
    order_date = Column(DateTime)
    status = Column(String(20))


