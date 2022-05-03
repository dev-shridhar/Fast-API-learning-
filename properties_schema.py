from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True                          #default True value 
    rating: Optional[int] = None                    #optional field,default value - None
    

@app.get("/getpost")
def get_post():
    return {"data": "This is your post"}

@app.post("/createpost")
def create_post(new_post : Post):
    print(new_post)
    print(new_post.dict())                          #returns data as in dictionary
    return {"data": new_post}