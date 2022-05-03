from fastapi import FastAPI, status, HTTPException
from typing import Optional
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = []
    
def find_post(id):
    for p in my_posts:
        if(p["id"] == id ):
            return p
        
@app.get("/getpost")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"pst of {id} not found")
        
@app.post("/createpost")
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict["id"] = randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
    