from typing import List
from fastapi import FastAPI, Path
import models
from database_logic import database, users, goods, orders

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=models.User)
async def create_user(user: models.UserIn):
    query = users.insert().values(user_name=user.user_name, user_surname=user.user_surname,
                                  user_email=user.user_email, user_password=user.user_password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "user_id": last_record_id}

@app.post("/goods/", response_model=models.Good)
async def create_good(good: models.GoodIn):
    query = goods.insert().values(good_name=good.good_name,
                                  description=good.description, price=good.price)
    last_record_id = await database.execute(query)
    return {**good.dict(), "good_id": last_record_id}

@app.post("/orders/", response_model=models.Order)
async def create_order(order: models.OrderIn):
    query = orders.insert().values(user_id=order.user_id, good_id=order.good_id,
                                   data=order.data, status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "order_id": last_record_id}

@app.get("/users/", response_model=List[models.User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@app.get("/goods/", response_model=List[models.Good])
async def read_goods():
    query = goods.select()
    return await database.fetch_all(query)

@app.get("/orders/", response_model=List[models.Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)

@app.get("/orders/{order_id}", response_model=models.Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.order_id == order_id)
    return await database.fetch_one(query)