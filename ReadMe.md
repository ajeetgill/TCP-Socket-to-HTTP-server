# HTTP Server Development with sockets - python

**AssignmentLvl1.md**

> 2023F CS-3420-01-Assignment 2
> HTTP Server Development

### Objectives

- learn and practice the basics of socket programming for TCP connections in Python
  - how to create a socket,
  - bind it to a specific address and port, as well as
  - send and receive a HTTP packet
- get familiar with HTTP request/response format.

### Deliverables : Web Server : `TCPServer.py`

> **_We assume no header lines are involved._**

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

You may expand the TCPServer.py provided in the github repo to implement the Web server.

> **Later,** not part of this `TCPserver.py` but in different branch.<br>
> TCPServer.py is expanded to,
>
> - http post-request server
> - inaccessible webpage (can only be seen after a form submission)
>
>   - this is also a template webpage - which substitute {{fname}} with data from form submission
>
> - [ ] gotta look into it
>   - multiple http connections
>   - technically, adding hot-reloading capability is a possibility
>     - similar to [VS-Code Live server (Readme)](https://github.com/tapio/live-server#readme)
>   - try making it accesible via internet (using ngrok)
>   - hosting it on a live URL accesible from anywhere on the internet.

## Provided Files

Test files are provided, and they should be put in the same directory that the server is in.

- TCPServer.py
  - this is a simple socket server in which the request message is any text line, and the response is the same text line but all letters are in upper case.
- TCPClient.py
  - a simple socket server in which the request message is any text line, and the response is the same text line but all letters are in upper case.
- index.html, flex.html - just to check that different routes are indeed working we will be using `form.html` later on. But
- form.html - as of now it's just to check (like flex.html)
  - other-git-branches : we will modify the server to handle POST requests
  - other-git-branches : return a templated-html(`success.html`) page populated from POST request response
  - other-git-branches : make the `success.html` be only accessible via form submission on `form.html`, visiting `success.html` directly will redirect to `form.html` with warning-text

## Test if working

Running the Provided Server, open terminal and type :

- `python3 file_name.py`

  <small>running TCPServer.py/TCPClient.py file will run server/client respectively</small>

#### FOR BASIC SERVER <small>Files provided in Repo</small> <hr>

- run server and client both are running.
- Sending some text(e.g. `test-text`) from client-temnial should output `TEST-TEXT` on the client-terminal.
  <br>Meanwhile the server-terminal should print `Requested Text: test-text`<br>

#### FOR HTTP-WEB-SERVER <hr />

UPPERCASE-transformation shouldn't be working anymore.

Run the server file, but for client - your **_Web-Browser_** is the client <br>TCPClient.py file isn't needed anymore at this point.

Open a browser, and type in the request : http://localhost:8000/index.html

All the test files should be successfully retrieved from the server.

> 💡Pro-tip : don't forget to close the things you open ;)

## Additional Information

In the WebServer, the request message is an HTTP GET request line. In the form of

`GET /filename HTTP/1.1
`

Please notice that this server only process GET, and does not care about the version, so that **_the only useful portion is the second portion: /filename_**

Obtain the filename. Any Python string process functions can be used, such as `split()`.

After the filename is retrieved from the message, you may want to open this file. Thus, python file processing functions, such as `open()`, should be used.

Different mechanisms can be used to determine if a file can be opened. One way is to use `try...except...finally` structure.

Run the server program. This server and the client may be in different hosts. Here we assume the server and the client are in the same host. Please use port 8000 instead of port 80.

> 👀 **HINT** 👀 <br>Printing the request you're getting from the client helps. In the TCPClient.py - you're the one sending some data to the TCPServer, but with web browser - think of it like, web browser already has some templated response ready (in the form of HTTP Get request).

<hr>

### Credit :

The original question was part of an assignment provided by [UPEI : Professor : Yingwei Wang](http://www.csit.upei.ca/~ywang/). I've changed it extensively and built on top of it. The original assignemt was just a simple http-get-server, but I messed around a bit, to see if I can make POST server and kept adding different capabilities.
