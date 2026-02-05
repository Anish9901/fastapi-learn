from enum import Enum

from fastapi import FastAPI

# Init fastapi
app = FastAPI()


# define root
@app.get("/")
async def root():
    return {"message": "Hello World"}


# path with param while enforcing typechecking
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# returns list
@app.get("/users")
async def get_users2():
    return ["abs", "asdf"]


# using enumerated paths
class Model(str, Enum):  # order of str and Enum matters, see __mro__.
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"
# print(Model.__mro__)


@app.get("/models/{model_name}")
async def get_model_name(model_name: Model):
    if model_name == Model.ALEXNET:
        return {"model_name": model_name, "message": "The very first model"}
    elif model_name.value == Model.RESNET:
        return {"model_name": model_name.value, "message": "The second model"}
    else:
        return {"model_name": model_name, "message": "residual"}


# file paths as params
@app.get("/files/{file_path:path}")  # no space around ":"
async def read_file(file_path: str):
    return {"file_path", file_path}
