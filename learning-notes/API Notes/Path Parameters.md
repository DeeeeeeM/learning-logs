You can declare parameters or variables using the same f"{variable}" fstring rule

`@app.get("/items/{item_id}") async def read_item(item_id): return {"item_id": item_id}`

You can also add types to it in the function argument

`async def read_item(item_id: int):`

FastAPI can give you the same data validation as Python.

If parameter input is a string and it requires an int, it will throw a nice JSON error.

If you have a Pydantic class, it can also handle the data validation for you.

**Order Matters**

You need to put Request methods which has parameters above the ones that dont

from fastapi import FastAPI

`@app.get("/users/me")
`async def read_user_me():
    `return {"user_id": "the current user"}`

`@app.get("/users/{user_id}")
`async def read_user(user_id: str):
    `return {"user_id": user_id}`

You can't redefine a path operation, can only be called once. First one will always be prioritized.

`@app.get("/users")
`@app.get("/users")

Predefined values
If you want to use a predefined parameter, use `enum`

**Enum** lets you create a fixed list of labels for your code, this avoids confusing magic numbers and messy text strings.

We use enum to let the API docs know that the valus must be a type of string. This can render it correctly.

You can compare enumeration member using if to direct it to a return for example.

You can also get its str value using .value

`from enum import Enum`

`Class ModelName(str, Enum): 
	`alexnet = "alexnet" 
	`resnet = "resnet" 
	`lenet = "lenet"`

`from enum import Enum
`from fastapi import FastAPI

`@app.get("/models/{model_name}")
`async def get_model(model_name: ModelName):
    `if model_name is ModelName.alexnet:
        `return {"model_name": model_name, `"message": "Deep Learning FTW!"}

    `if model_name.value == "lenet":
        `return {"model_name": `model_name, "message": "LeCNN all the images"}

    `return {"model_name": model_name, `"message": "Have some residuals"}

You can view the predefined path parameter in the **interactive docs.**

**Path support**
You can declare a path using `/files/{file_path:path}`

For summary, 

By using python type declarations, you can validate data, data parsing, check for errors, incomplete data.

Then, FastAPI handles API annotation and automatic documentation