from fastapi import FastAPI, Response, status, HTTPException
from typing import Optional
from pydantic import BaseModel
from random import randrange
 
app = FastAPI()

my_posts = []

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int]

@app.get("/allposts")
def get_all_posts():
    return {"data": my_posts}
    
@app.get("/getpost/{id}")
def get_post(id: int):
    for p in my_posts:
        if p["id"] == id:
            return {"data": p}
    return {"data" : "post not found"}


@app.post("/createpost")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(1,100000000)
    my_posts.append(post_dict)
    return {"data": post_dict} 

@app.delete("/deletepost/{id}")
def delete_post(id: int):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            my_posts.pop(i)
    return Response(status_code=status.HTTP_204_NO_CONTENT)    