HTTP - Application layer protocol operating in a server where a client connects > sends a request > waits and receive a response

Basically HTTP is a app layer that operates in a server where it handles client requests and sends a response from a requested service.

HTTP is stateless, no session data between separate requests

**HTTP Request Methods (REST APIs)**
Contains different actions to indicate a clients request
- GET
- POST
- PUT
- PATCH
- DELETE

There are also other actions:
- HEAD
- OPTIONS
- TRACE
- CONNECT

**HTTP Status Codes**
- 2xx (Success): `200 OK`, `201 Created`, `204 No Content`, `206 Partial Content`
- 3xx (Redirection): `301 Moved Permanently`, `302 Found`, `304 Not Modified`
- 4xx (Client Errors): `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `405 Method Not Allowed`, `422 Unprocessable Content` (data validation errors), `429 Too Many Requests`
- 5xx (Server Errors): `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeou`

These are basically traffic lights where a server lets through your request. 
Green (2xx) if no there are no issues. 
Yellow (4xx) if there are issues
Red (5xx) if there are server issues

**HTTP Caching & Conditional Requests**
Server can send a Set-Cookie header in responses, client stores this and attaches to subsuquent request using the Cookie to maintain its session state over a stateless protocol.

Basically a hand stamp given to an amusement park gate. When you exit to buy something outside, you can re-show the stamp to let them know you already entered earlier.

**Payload Compression:**
Message are compressed before being transmitted, it uses header to improve transfer speeds.

Just like packing your clothes in a luggage, you need to vaccuum seal them to save space.

**Range Requests & Partial Content**
Using a Range request header, clients can request specific resources to the server.

Basically just asking a certain part of a book. 

**Content Negotiation**
Clients can specify which type of resource format the client can handle

**Authentication & Security Headers**
Web security policies are enforced via headers to ensure malicious access can't penetrate your server.

**Cross-Origin Resource Sharing (CORS)**
Security mechanish that allows a web server to permit a web app from a different domain, protocol, or port to access its restricted resources.

Basically an app talking to different or another api

**Proxy Servers, Gateways & Load Balancers**
Traffic management system that handle routing, security and scalability. Like how a mailroom works, receptionist receives a package, mailroom signs it and notes down who sent it, and passes it in the inner office.