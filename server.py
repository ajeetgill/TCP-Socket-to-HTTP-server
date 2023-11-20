from socket import *
import urllib.parse

# GLOBAL VARIABLES
request_count = 0
SERVER_PORT = 8000

# parse_form_data : data in the form is in the format: fname=John&lname=Doe
def parse_form_data(form_data):
     form_data_dict = {}
     pairs = form_data.split('&')
     for pair in pairs:
          key, value = pair.split('=')
          value = urllib.parse.unquote(value.replace('+', ' '))
          form_data_dict[key] = value
     return form_data_dict


# get_content_length : returns the content length from the request headers
def get_content_length(request):
    for line in request.split('\r\n'):
        if line.startswith('Content-Length: '):
            content_length = int(line.split(': ')[1])
            return content_length
    return None


# returns the request based on if it was GET or POST request
def handle_request(connectionSocket):
     init_data_received = 100
     default_data_size = 1024
     data_left = default_data_size - init_data_received

     request = connectionSocket.recv(init_data_received).decode('utf-8')
     request_lines = request.split('\r\n')
     
     # Extract the HTTP method from the request line
     method, relative_filename, version = request_lines[0].split()

     if(method == "GET"):
          request += connectionSocket.recv( data_left ).decode('utf-8')
     elif(method == "POST"): # returns based on Content-Length in the request header
          content_length = get_content_length(request)
          if content_length is not None:
               # Read the form data according to the content length
               request += connectionSocket.recv(data_left + content_length).decode('utf-8')
     
     request_lines = request.split('\r\n')
     return method, relative_filename, version, request_lines


# handle_get: returns the response for GET request
def handle_get(file_to_serve):
     response = ""
     try:
          if(file_to_serve == ""):
               file_to_serve = "index.html"

          # making sure that success.html is served only when processing POST request
          elif(file_to_serve == "success.html"):
               file_to_serve= "form.html"
          with open(file_to_serve, 'rb') as file:
               data = file.read()  # Read the file content
               # Do something with the file data
               response = "HTTP/1.1 200 OK\r\n\r\n".encode('utf-8') + data

     except FileNotFoundError:
          print("'"+file_to_serve+"'- File not found.")
          response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found.".encode('utf-8')

     except Exception as e:
          print(f"An error occurred: {e}")
          response = "HTTP/1.1 404 Not Found\r\n\r\nAn error occurred.".encode('utf-8')

     finally:
          if 'file' in locals():
               file.close()  # Close the file if it's open
          return response


# handle_post: returns the response for POST request
def handle_post(request_lines):
     # get the form data
     form_data = parse_form_data(request_lines[-1])
     print(f"__{request_count} : form_data={form_data}")
     fname = form_data.get('fname')
     lname = form_data.get('lname')

     respone_data = None
     try:
          with open("success.html", 'rb') as file:
               respone_data = file.read()  # Read the file content
               respone_data = respone_data.replace(b'{{fname}}', fname.encode('utf-8'))
               respone_data = respone_data.replace(b'{{lname}}', lname.encode('utf-8'))
     except FileNotFoundError:
          error("'success.html'- File not found.")
     
     # Construct an HTTP response
     response_message = "Form submission received. Thank you.\n"
     if respone_data is not None:
          # response = f"HTTP/1.1 200 OK\r\n\r\n{respone_data}"
          response = "HTTP/1.1 200 OK\r\n\r\n".encode('utf-8') + respone_data
     else:
          response = f"HTTP/1.1 200 OK\r\n\r\n{response_message}{form_data}".encode('utf-8')   # the response has to be in bytes - hence encode('utf-8')
     return response 


def start_server():
     serverSocket = socket(AF_INET,SOCK_STREAM)
     serverSocket.bind(('',SERVER_PORT))
     serverSocket.listen(1)
     print ('Server is ready to serve on port:',SERVER_PORT,' !!!')
     print('Entering infinite loop; hit CTRL-C to exit')

     try:
          while True:
               connectionSocket, addr = serverSocket.accept()
               method, relative_filename, version, request_lines = handle_request(connectionSocket)

               #increment the request count
               global request_count 
               request_count += 1
               if(request_count < 10):
                    print(f"r_0{request_count} :",method, relative_filename, version)
               else:
                    print(f"r_{request_count} :",method, relative_filename, version)


               if method == "GET":
                    file_to_serve = relative_filename[1:]
                    response = handle_get(file_to_serve)
                    
               elif method == "POST":
                    response = handle_post(request_lines)
               else:
                    # If content_length is not provided, handle the error accordingly
                    response = "HTTP/1.1 400 Bad Request\r\n\r\nContent-Length not provided.".encode('utf-8')

               connectionSocket.sendall(response)
               connectionSocket.close()

     except KeyboardInterrupt:
          print("\nOuch!!! - Server terminated by user!!!")
     finally:
          serverSocket.close()

start_server()