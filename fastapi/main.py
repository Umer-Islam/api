from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.get("/")
def root():
    return "...wabbalabba..."

@app.get("/notroot")
def notroot():
    return {"whatever":"smileEmoji"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return{"new post created": f"title: {payload['title']}, content:{payload['content']}"}