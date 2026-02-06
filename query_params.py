from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "query_params"}

db_dict = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "Bat"}
]


# default query params
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return db_dict[skip:skip + limit]


# optional query param q
@app.get("/items/{item_id}")
async def read_item2(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# boolean query param short
@app.get("/items/bool/{item_id}")
async def read_item3(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is a long description"}
        )
    return item


# multiple path and query params
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is a long description"}
        )
    return item


# required query param
@app.get("/items/required/{item_id}")
async def get_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
