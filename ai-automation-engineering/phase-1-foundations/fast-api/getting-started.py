from fastapi import FastAPI

app = FastAPI()

#Decorator or "instance" - @app
#http method - .get - send get request
#Path - ("/") - path to go to 
@app.get("/") 

#Function with async
async def root():
    #Function body
    return {"message": "Hello World"}

@app.get("/posts")
def get_userdata():
        return{"data": "A user commented on your post!"}

# http://******:8000/posts
# {"data":"A user commented on your post!"}

    
