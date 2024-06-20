from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()


class post(BaseModel):
    title: str
    content: str
    rating: Optional[int] = None
    

my_posts = [
    {"title": "title of post 1 ", "content": "content of post 1", "id": 1},
    {"title": "title of post 2 ", "content": "content of post 2", "id": 2},
    {"title": "title of post 3 ", "content": "content of post 3", "id": 3},
]


@app.get("/")
def root():
    return "...wabbalabba..."


@app.get("/posts")
def get_post():
    return {"your_posts ": my_posts}


@app.post("/posts")
def create_post(Post: post):
    my_dict = Post.dict()
    my_dict['id'] = randrange(1,10000000)
    my_posts.append(my_dict)
    # print(f" {my_dict}")
    return {"new post created": my_dict}
