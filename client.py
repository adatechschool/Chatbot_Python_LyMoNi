import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ip and port of the server
host = '127.0.0.1'
port = 13

#connection to the server
client.connect((host, port))

#transmission of the information
info = 'Hello world'

client.send(info.encode())
information = client.recv(1024)
print(information.decode())
