from fastapi import FastAPI, Response, status, HTTPException
from typing import Optional
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]
    
my_posts = []

@app.get("/getpost/{id}")
def get_post(id: int):
    for p in my_posts:
        if p["id"] == id:
            return {"data": p}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/allposts")
def all_posts():
    return {"data": my_posts}
  
@app.post("/createpost")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(1,1000000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.put("/update/{id}")
def update_post(id: int, post:Post):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            post_dict = post.dict()
            post_dict["id"] = id
            my_posts[i] = post_dict
            return {"data": post_dict}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND) 

@app.delete("/delete/{id}")
def deleete_post(id: int):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            my_posts.pop(i)
            return {"data": "post is deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)