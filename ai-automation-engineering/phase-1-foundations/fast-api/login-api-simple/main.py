from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from random import randrange

#USER SCHEMA
class User(BaseModel):
    username: str = Field(
        ..., 
        min_length=3,
        max_length=50, 
        pattern="^[a-zA-Z0-9_]+$", 
        description="Username must be 3-50 characters long and can only contain letters, numbers, and underscores."
    )
    email: str
    password: str = Field(min_length=8)
    status: str = "logged out"
    
#LOGIN SCHEMA
class LoginRequest(BaseModel):
    username: str = Field(..., description="The username of the user trying to log in.")
    password: str = Field(..., description="The password of the user trying to log in.")

app = FastAPI() 

#USER DB
users_db= [{
    "id": 1,
    "username": "admin",
    "email": "admin@email.com", 
    "password": "admin123",
    "status": "logged out"
}]

def data_check(field, value):
    for i in users_db:
        if i[f'{field}'] == value:
            return i, 

def find_user_index(id):
    for index, user in enumerate(users_db):
        if id == user['id']:
            return index

#USER CREATION
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    
    user_dict = user.model_dump()
    
    if data_check("username", user_dict['username']):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail=f"Username {user_dict['username']} is taken, try again!")

    user_dict['id'] = randrange(0, 99999)
    user_dict['status'] = "logged out"
    users_db.append(user_dict)
    
    return {'data': user_dict}

@app.get("/users", status_code=status.HTTP_200_OK)
def get_users():
        return {'data': users_db}
    
@app.get("/users/logged-in", status_code=status.HTTP_200_OK)
def check_logged_in():
    return {'data': [i for i in users_db if i['status'] == 'logged in']}   
    
@app.get("/users/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int):
    
    user_data = data_check("id", id)
    
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="ID not found")
    
    return {"data": user_data}

@app.post("/login", status_code=status.HTTP_200_OK)
def login_user(login_user: LoginRequest):
    
    login_data = login_user.model_dump()
    user_data = data_check("username", login_data['username'])
    
    if not user_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    if login_data['password'] == user_data['password']:
        user_data['status'] = "logged in"
        return {'message': "Login successful"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.post("/users/logout/{id}")
def logout_user(id: int):
    
    user_data = data_check("id", id)
    
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    elif user_data['status'] == "logged out":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already logged out")
    else:
        user_data['status'] = "logged out"
        return {'message': "Successfuly logged out"}

@app.put("/users/{id}")
def update_user(id: int, user: User):
    
    user_data = data_check("id", id)
    
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    update_data = user.model_dump()
    exisitng_user = data_check("username", update_data['username'])
    
    if exisitng_user and exisitng_user['id'] != user_data['id']:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists!")
    
    user_data['username'] = update_data['username']
    user_data['email'] = update_data['email']
    user_data['password'] = update_data['password']
    return {"message": "User information updated!"}

@app.delete("/users/{id}", status_code=status.HTTP_200_OK)
def delete_user(id: int, user: User):
    
    user_data = data_check("id", id)
    
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user_index = find_user_index(user_data['id'])
    users_db.pop(user_index)    
    return {'message': f"User {user_data['username']} is deleted!"}