from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Starter")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


# In-memory storage for assignment practice.
items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment starter."}


@app.get("/items")
def list_items():
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


@app.post("/items")
def create_item(payload: ItemCreate):
    item = payload.model_dump()
    items.append(item)
    return {"item": item, "id": len(items) - 1}
