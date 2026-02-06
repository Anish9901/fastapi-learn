from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# request body schema def using pydantic BaseModel
class Item(BaseModel):
    name: str  # required
    description: str | None = None  # optional with default = None
    price: float  # required
    tax: float | None = None  # optional with default = None


# validate the request body using the Item model as a param
@app.post("/items/")
async def create_item(item: Item):
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict = item.model_dump()
        item_dict.update({"price_with_tax": f"${price_with_tax}"})
        return item_dict
    return item


# validate request body, path, query params
@app.put("/items/{item_id}")
async def update(item_id: int, item: Item, q: str | None = None):
    res = {"item_id": item_id, **item.model_dump()}
    if q:
        res.update({"q": q})
    return res
