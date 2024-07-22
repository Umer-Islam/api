from fastapi import FastAPI,Response,status,HTTPException
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
    {"title": "title of post 1 ", "content": "content of post 1", 'id':1},
    {"title": "title of post 2 ", "content": "content of post 2", 'id':2},
    {"title": "title of post 3 ", "content": "content of post 3", 'id':3},
]


@app.get("/")
def root():
    return "...wabbalabba..."


@app.get("/posts")
def get_post():
    return {"your_posts ": my_posts}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(Post: post):
    my_dict = Post.dict()
    my_dict['id'] = randrange(1,10000000)
    my_posts.append(my_dict)
    # print(f" {my_dict}")
    return {"new post created": my_dict}

# fetching one single post
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        

@app.get("/post/{id}")
def get_one_post(id:int):
    """ ,response:Response """ #use this parameter in case of second option, dont forget to import
    post = find_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
        # OR
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id:{id} not found"}
    print(post)
    return {"post Fetched!": post}
#delete post
def find_index(id):
        for i, p in  enumerate(my_posts):
            if p['id'] ==id:
                return i

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post (id: int):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} doesn't exist")

    my_posts.pop(index)
    # here trying to return anything will result in error
    return Response(status_code=status.HTTP_204_NO_CONTENT)