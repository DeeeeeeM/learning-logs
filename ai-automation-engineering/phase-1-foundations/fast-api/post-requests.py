#GET - gettings data from API serve
#POST - Sending data to API server

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

#Defies the schema
class Post(BaseModel):
    title: str
    content: str    
    published: bool = True #Can define default value
    rating: Optional[int] = None #Optional field, can be null

@app.get("/") 
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_userdata():
        return{"data": "A user commented on your post!"}

@app.post("/createposts")
#new_post stores data as a pydantic model
def create_posts(post: Post):
    print(post)
    #to convert to a dict use new_post.dict()
    return {"data": post}

