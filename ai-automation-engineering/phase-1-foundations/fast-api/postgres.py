#GET - gettings data from API serve
#POST - Sending data to API server

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 

app = FastAPI()

#Defies the schema
class Post(BaseModel):
    title: str
    content: str    
    published: bool = True #Can define default value
    rating: Optional[int] = None #Optional field, can be null

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error ", error)
        time.sleep(3)

@app.get("/") 
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return{"data": posts}

#/posts/ is a path parameter, can be declared again
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    
    cursor.execute("SELECT * FROM posts WHERE serial = %s", (str(id)))
    post = cursor.fetchone()
    
    #To handle data that does not exist, use HTTPException and status 404
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post was not found")
        
    return {"post_detail": post}

# Note: 
# - Everything that fastapi returns is a str
# - Be mindful of order of get requests (It works Top to Bottom) 

# When creating data should always send back 201
@app.post("/posts", status_code=status.HTTP_201_CREATED)

#new_post stores data as a pydantic model
def create_posts(post: Post):
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * ", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

#Deleting post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    
    cursor.execute("DELETE FROM posts WHERE serial = %s RETURNING *", (str(id)))
    deleted_post = cursor.fetchone()
    
    #Handler for data that does not exist
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post does not exist")
    
    conn.commit()
    
    # If it is 204 or DELTE, dont send data back, send a status code
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#Update post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    
    cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE serial = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post does not exist")
    
    conn.commit()
    return {'data': updated_post}
    
