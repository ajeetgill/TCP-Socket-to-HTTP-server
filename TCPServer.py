from socket import *
serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
print ('localhost:8000')
request_count = 0

try:
     while True:
          #  accept the incoming HTTP get request from the client and decode it
          connectionSocket, addr = serverSocket.accept()
          request = connectionSocket.recv(1024).decode('utf-8')
          #  parse the request to determine the specific file being requested from the client
          request_lines = request.split('\n')
          http_request_line = request_lines[0].split()
          method, relative_filename, version = http_request_line
          file_to_serve = relative_filename[1:]

          response = ""
          request_count += 1
          try:
               if(file_to_serve == ""): # if no file is specified, serve index.html
                    # file_to_serve == "" 
                    # it's a common practive that if there's no file specified, the server will serve the index.html file so I added this rule
                    file_to_serve = "index.html"

               with open(file_to_serve, 'rb') as file: 
                    data = file.read()  # Read the file content
                    print(request_count,"Serving file:",file_to_serve)
                    response = "HTTP/1.1 200 OK\r\n\r\n".encode('utf-8') + data

          except FileNotFoundError:
               print(request_count,"'"+file_to_serve+"'- File not found.")
               response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found : File not found.".encode('utf-8')

          except Exception as e:
               print(f"{request_count} An error occurred: {e}")
               response = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found : Unknown error occurred.".encode('utf-8')

          finally:
               if 'file' in locals():
                    file.close()  # Close the file if it's open
          
          connectionSocket.sendall(response)
          connectionSocket.close()

except KeyboardInterrupt:
     print("\nServer terminated.\nTotal GET Requests:",request_count,"\n")

finally:
    serverSocket.close()