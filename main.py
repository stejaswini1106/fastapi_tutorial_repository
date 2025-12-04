from fastapi import FastAPI, HTTPException #import FastAPI and use that to create a new app
from pydantic import BaseModel
app = FastAPI()

items = []

class Item(BaseModel):
    text: str = None
    is_done: bool = False

#define a path in fastapi using decorator @, when we hit this, the below fun will be called
@app.get("/") 
def root():
    return{"Hello Wolrd"}

#new end point for app, to give data
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

#request and path parameters
@app.get("/items", response_model= list[Item])
def list_items(limit: int = 2):
    return items[0:limit]


#to view specific item on the list
@app.get("/items/{item_id}", response_model= Item)
def get_item(item_id: int):
    if item_id < len(items):      # item= item[item_id] return item
        return items[item_id]
    else:     #HTTP response status code, client error response
        raise HTTPException(status_code=404, detail= f"Item {item_id} is not found")
    
# to read all the items in the list
@app.get("/items")
def get_all_items():
    return items