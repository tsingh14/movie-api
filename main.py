from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    int1 : int
    int2 : int

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World!"}

@app.get("/items/{item_id}")
def return_item(item_id):
    return item_id

@app.post("/sum")
def sum_item(item : Item):
    return item.int1+ item.int2
