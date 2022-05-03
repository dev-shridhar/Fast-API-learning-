from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    
@app.get("/getpost")
def get_post():
    return {"data" : "This is your post"}

@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post)
    return {"new_post": new_post}