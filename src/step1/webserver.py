from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serverSocket.bind(('', 679)) # 将TCP欢迎套接字绑定到指定端口
serverSocket.listen(1) # 最大连接数为1
print('start...')
conn,address = serverSocket.accept()
print("连接成功")
message = conn.recv(1024) # 获取客户发送的报文
conn.send('hello world'.encode())
conn.close()
