#GET - gettings data from API serve
#POST - Sending data to API server

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

#Defies the schema
class Post(BaseModel):
    title: str
    content: str    
    published: bool = True #Can define default value
    rating: Optional[int] = None #Optional field, can be null

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/") 
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
        return{"data": my_posts}

# When creating data should always send back 201
@app.post("/posts", status_code=status.HTTP_201_CREATED)

#new_post stores data as a pydantic model
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 9999999)
    my_posts.append(post_dict)
    return {"data": post_dict}

#/posts/ is a path parameter, can be declared again
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))
    
    #To handle data that does not exist, use HTTPException and status 404
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
       
    return {"post_detail": post}

# Note: 
# - Everything that fastapi returns is a str
# - Be mindful of order of get requests (It works Top to Bottom) 


#Deleting post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #find the index in the array that has required id
    index = find_index_post(id)
    
    #Handler for data that does not exist
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    my_posts.pop(index)
    
    # If it is 204 or DELTE, dont send data back, send a status code
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#Update post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict    
    return {'data': post_dict}
    
