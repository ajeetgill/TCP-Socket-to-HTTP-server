# Solution to HTTP Server Development with sockets - python

**[Original Full Question/Task Link](https://github.com/ajeetgill/http-server-tcp-socket-python#http-server-development-with-sockets---python)**

This is built on top of a project which you can find at the above provided link <br>OR <br>
in branch named `tcp-http-get-server` in present github repo.

## Test if working

Running the Provided Server, open terminal and type :

- `python3 TCPserver.py`

Run the server file, once you see text:
`'The server is ready to receive
localhost:8000'`

Open a browser, and type in the request : http://localhost:8000/index.html

All the test files should be successfully retrieved from the server.

## Final : Web Server : `TCPServer.py`

> **_We assume no header lines are involved._**

TCPServer.py, requirements met:

- a simple http server which parses http-get request from browser and serves the relevant file
- that handles one HTTP request at a time
- should accept and parse the HTTP request,
  - get the requested file from the server’s file system,
  - create an HTTP response message which contains the requested file, and then
  - send the response directly to the client.
  - If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client.
- if no file is specified - i.e. [http://localhost:8000](http://localhost:8000/), then the server should return `index.html`
- If file is sent - a 200 response message should be sent back
- If file does not exist - a 404 response message should be sent back
- If any other error occurs - a 404 response message should be sent back
