# POST-http server development with sockets - python

**[Original Full Question/Task Link](https://github.com/ajeetgill/http-server-tcp-socket-python#http-server-development-with-sockets---python)**

This is built on top of a project which you can find at the above provided link <br>OR <br>
in branch named `0-tcp-http-get-serve` in present github repo.

## Test if working

Running the Provided Server, open terminal and type :

- `python3 TCPserver.py`

Run the server file, once you see text:
`'The server is ready to receive
localhost:8000'`

Open a browser, and type in the request : http://localhost:8000/index.html

All the test files should be successfully retrieved from the server.

## Final : Web Server : `PostServer.py`

Basically the next thing we're gonna do to upgrade our server.

> **_Building on top of `TCPServer.py` - (GET handler). <br>
> Some header lines are involved, when dealing with POST._**

Requirements:

- [ ] Upon submitting the form in `form.html`, the server should display the relevant fields from the form in console
- [ ] return the _`form_data`_ to User - visible in their web browser
- [ ] Create a templated `success.html` which gets populated with User Data before being returned to user

> 💡 `PostServer.py` - included to see the final result implement with above things

## Further ideas to expand -

- [ ] POST request should be processed only if coming from `form.html`
- [ ] `/api`/ route - which return different data [GET and POST]
