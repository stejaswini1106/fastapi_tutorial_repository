from fastapi import FastAPI

app = FastAPI()

items= []

@app.get("/")
def root():
    return{"Hello... Welcome"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

@app.get("/items")
def get_all_items():
    return items