import socket
s = socket.socket()
host = socket.gethostname()
port = 6789
s.connect((host, port))
s.send("GET /HelloWorld.html HTTP/1.1\r\n".encode())
s.close()