from datetime import datetime
from pydantic import BaseModel, Field

class UserIn(BaseModel):
    first_name: str
    second_name: str
    email: str
    password: str

class User(UserIn):
    id: int

class OrderIn(BaseModel):
    user_id: int
    product_id: int
    status: str

class Order(OrderIn):
    id: int

class ProductIn(BaseModel):
    name: str
    description: str
    price: float

class Product(ProductIn):
    id: int