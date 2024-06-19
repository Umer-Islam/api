from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None

@app.get("/")
def root():
    return "...wabbalabba..."

@app.get("/notroot")
def notroot():
    return {"whatever":"smileEmoji"}

@app.post("/posts")
def create_post(Post:post):
    print(Post)
    print(Post.dict()) # turns the data into a python dictionary
    return{"new post created"}