import socket
import tools as tls

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#assign ip and port of the server
server.bind(('127.0.0.1', 13))

server.listen() #paramter? -> 5

while True:
    connection, address = server.accept()
    print('Client is connected to: ', address)

    while True:
        data = connection.recv(1024)

        data = data.decode()

        comm = data.split(' ', 1)

        if comm[0] in tls.commands:
            tls.tools(data) 

        if data == 'stop':
            connection.send(data)
            print('exit')
            break

        connection.send(data.encode())

    connection.close()
    if connection.fileno() == -1: # check if client connection is closed
        print("Client connection closed.")
