from datetime import datetime
from pydantic import BaseModel, Field

class UserIn(BaseModel):
    user_name: str = Field(max_length=32)
    user_surname: str = Field(max_length=64)
    user_email: str = Field(max_length=128)
    user_password: str = Field(max_length=16)
class User(BaseModel):
    user_id: int
    user_name: str = Field(max_length=32)
    user_surname: str = Field(max_length=64)
    user_email: str = Field(max_length=128)
    user_password: str = Field(max_length=16)

class GoodIn(BaseModel):
    good_name: str = Field(max_length=64)
    description: str = Field(max_length=128)
    price: float
class Good(BaseModel):
    good_id: int
    good_name: str = Field(max_length=64)
    description: str = Field(max_length=128)
    price: float

class OrderIn(BaseModel):
    user_id: int
    good_id: int
    data: datetime
    status: str = Field(max_length=32)
class Order(BaseModel):
    order_id: int
    user_id: int
    good_id: int
    data: datetime
    status: str = Field(max_length=32)