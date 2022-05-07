from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
app = FastAPI()

try:
    conn = psycopg2.connect(host='localhost', 
                            database='fastapi', 
                            user='postgres', 
                            password='12345678',
                            cursor_factory= RealDictCursor)
    cursor = conn.cursor()
    print("Database connection is successfull")
except Exception as error:
    print("Conenction to databse failed")
    print( "Error", error)
    
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
@app.get("/get/{id}")
def get_post(id: int):
    try:
        cursor.execute("SELECT * FROM posts WHERE id= %s",(str(id)))
        post = cursor.fetchone()
        print(post)
        return {"data": post}
    except Exception as error:
        print("Post not found")
        print("Error: ",error)
        
@app.get("/getall")
def get_all_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}
    
@app.post("/create_post")
def create_post(post: Post):
    cursor.execute("INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *",
                   (post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@app.delete("/deletepost/{id}")
def delete_post(id: int):
    cursor.execute("DELETE FROM posts WHERE id= %s RETURING *",(str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    return {"data": deleted_post}

@app.put("/update/{id}")
def update_post(id: int, post=Post):
    cursor.execute("UPDATE posts SET title=%s,content=%s,published=%s WHERE id=%s RETURNING *", 
                   (post.title,post.content,post.published,str(id)))
    updated_post = cursor.commit()
    conn.commit()
    return {"data": updated_post}
    