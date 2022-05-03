from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/getpost")
def get_post():
    return {"data" : "This is your post"}

@app.post("/createpost")
def create_post(payload : dict = Body(...)):
    print(payload)
    return {"new_post" : f"tile: {payload['title']}, content: {payload['content']}" } 