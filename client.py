import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ip and port of the server
host = '
port = 13

#connection to the server
client.connect((host, port))

#transmission of the information

print("Type 'stop' to close the connection \n")

while True:
    info = input('>> ')
    client.send(info.encode())
    information = client.recv(1024)
    if information.decode() == 'stop':
        break
    print(information.decode())
