When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

Query is set of key-value pairs that go after the ? separated by & in a URL.

These query parameters can have default values assigned by =

```
`async def read_item(skip: int = 0, limit: int = 10):
```

- `skip`: with a value of `0`
- `limit`: with a value of `10`
URL : 'http://127.0.0.1:8000/items/?skip=0&limit=10'

Basically type conversions can also become variables.

They can also have **Optional Parameters** by using None

```
async def read_item(item_id: str, q: str **| None = None**): 
	if q: 
		return {"item_id": item_id, "q": q} 
	return {"item_id": item_id}
```

You can also have **bool types**

```
async def read_item(item_id: str, q: str | None = None, short: bool = False):
```

```
http://127.0.0.1:8000/items/foo?short=true
```

You can go all out by declaring as many variables as you want.

```
async def read_user_item( 
	user_id: int, item_id: str, q: str | None = None, short: bool = False 
):
```

When you have a required parameter, you could get an error since it will require an argument of a certain type

```
async def read_user_item(item_id: str, needy: str):
```

```
http://127.0.0.1:8000/items/foo-item
```

```
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "needy"
      ],
      "msg": "Field required",
      "input": null
    }
  ]
}
```