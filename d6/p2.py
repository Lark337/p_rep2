from fastapi import FastAPI
from sqlalchemy import create_engine, select, insert, update, delete
import databases

from d6.sql_models import Base, User as SUser,Order as SOrder ,Product as SProduct
from d6.pydantic_models import UserIn,User,ProductIn,Product,OrderIn,Order

DATABASE_URL = 'sqlite:///d6/instance/database.db'

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind=engine)

app = FastAPI()

async def create(item, sitem):
    new = insert(sitem).values(**item.model_dump())
    await database.execute(new)

    return item

async def get_items(sitem):
    items = select(sitem)

    return await database.fetch_all(items)

async def get_item(item_id:int,sitem):
    item = await database.fetch_one(select(sitem).where(sitem.id == item_id))
    return item

async def update_item(item_id,new_item,sitem):
    item_update = (
        update(sitem)
        .where(sitem.id == item_id)
        .values(**new_item.model_dump())
    )
    await database.execute(item_update)

    return await database.fetch_one(select(sitem).where(sitem.id == item_id))

async def delete_item(item_id,sitem):
    delete_item = delete(sitem).where(sitem.id == item_id)

    await database.execute(delete_item)

    return {'result': 'success', 'deleted': item_id}

@app.get('/users/', response_model=list[User])
async def get_users():
    users = select(SUser)

    return await database.fetch_all(users)


@app.post('/users/', response_model=UserIn)
async def create_user(user: UserIn):
    await create(user,SUser)
    return "new_user"


@app.get('/users/{user_id}', response_model=User)
async def get_user(user_id: int):
    return await get_item(user_id,SUser)


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    return await update_item(user_id,new_user,SUser)


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    await delete_item(user_id,SUser)
    return {'result': 'success', 'deleted': user_id}


@app.get('/products/', response_model=list[Product])
async def get_products():
    return await get_items(SProduct)


@app.post('/products/', response_model=ProductIn)
async def create_product(product: ProductIn):
    await create(product,SProduct)
    return "new_product"


@app.get('/product/{product_id}', response_model=Product)
async def get_product(product_id: int):
    return await get_item(product_id,SProduct)


@app.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    return await update_item(product_id,new_product,SProduct)


@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    await delete_item(product_id,SProduct)
    return {'result': 'success', 'deleted': product_id}


@app.get('/orders/', response_model=list[Order])
async def get_orders():
    return await get_items(SOrder)


@app.post('/orders/', response_model=OrderIn)
async def create_order(order: OrderIn):
    await create(order,SOrder)
    return "new_order"


@app.get('/orders/{order_id}', response_model=OrderIn)
async def get_order(order_id: int):
    return await get_item(order_id,SOrder)


@app.put('/orders/{order_id}', response_model=OrderIn)
async def update_order(order_id: int, new_order: OrderIn):
    return await update_item(order_id,new_order,SOrder)


@app.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    await delete_item(order_id,SOrder)
    return {'result': 'success', 'deleted': order_id}