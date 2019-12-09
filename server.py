import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#assign ip and port of the server
server.bind(('127.0.0.1', 13))

server.listen() #paramter? -> 5

while True:
    connection, address = server.accept()
    print('Client is connected to: ', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(data)
    connection.close()
server.close()
