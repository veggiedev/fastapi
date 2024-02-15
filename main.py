from pydantic import BaseModel
from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Optional
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world!"}


# @app.post("/")
# async def post():
#     return {"message":"hello from the post route"}
#
# @app.put("/")
# async def put():
#     return {"message": "hello from the put route"}
#
# # @app.get("/users")
# # async def list_items():
# #     return {"message": "list items route"}
# #
# @app.get("/users/me")
# async def get_current_user():
#     return {"message": "this is the currents user"}
#
# @app.get("/users/{user_id}")
# async def get_items(item_id: int):
#     return {"item_id":item_id}
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dary"
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
#     elif food_name.value == "fruits":
#         return {"food_name": food_name, "message": "you are still healthy but like fruits"}
#     return {"food_name": food_name, ",essage": "I like milk"}
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name":"Baz"},]
#
#
# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "lorem ipsum jbnedfiuw fkrwiufb kiurgbf fbri iubrewf iubrf"})
#     return item
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item:Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result

class Item(BaseModel):
    name: str
    description : str  | None = None
    price: float
    tax: float

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
    q: str | None = None,
    item: Item | None = None,
    user: User
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item":item})
    if user:
        results.update({"user":user})
    return results
