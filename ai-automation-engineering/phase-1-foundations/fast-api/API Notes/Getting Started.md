# Quick Start

Import the FAST API library
`from fastapi import FastAPI

<mark style="background: #FFF3A3A6;">Create an instance</mark> or application object
`app = FastAPI()
Packing all the features, helpers, functions, rules into one object

Route Decorator
`@app.get("/")

A "decorator" takes the function below and does something with it. It means go to the path "/" using GET operator.

Defines the last part of your URL starting from "/"

Common HTTP methods
- `POST` `@app.post()` - Insert
- `GET` `@app.get()` - Select
- `PUT` `@app.put()` - Update
- `DELETE` `@app.delete()` - Delete

<mark style="background: #FFF3A3A6;">asynchronous path operation function</mark>
`async def root():
It means working with other tasks while a task requested by a customer is processing or in restaurant setting, cooking
**FastAPI** calls this function whenever it receives a request

Note: Can also be defined as def root():, it will work just fine. However, it will do tasks one by one like how it was in default.

return a JSON object represented as a dictionary
    `return {"message": "Hello World"}`

You can return a `dict`, `list`, singular values as `str`, `int`, etc.

# Run Server

To run <mark style="background: #FFF3A3A6;">server</mark>: `uv run fastapi dev

for **<mark style="background: #FFF3A3A6;">documentation</mark>** visit /[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

# **OpenAPI** standard for defining APIs.

Basically you're viewing a menu, tell the waiter what you want, and bring you your order. Open API is the menu and JSON Data Schema is the recipe booklet / procedure.

**REST APIs** - Allows 2 or more applications to talk to each other using HTTP rules / protocols. 

**Schema** - means a blueprint to make everything organized, will throw an error if there's a stucture issue.

**API schema** - makes REST APIs readable in a JSON format.

**Data schema** - contains JSON attributes, data types, validation, required and optional fields.

# [RECOMMENDED] Configure app entrypoint in pyproject.toml

```
[tool.fastapi]
entrypoint = "main:app"
```

This lets FastAPI visit pyproject.toml first to open your app. This prevents it to not search around your project and got to your specified entry path.



