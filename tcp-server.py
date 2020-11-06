#!/usr/bin/python3

import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
host = socket.gethostname()
print('Host name: ' + host)
port = 8081

server.bind((host, port))

server.listen(5)

while True:
    client, address = server.accept()
    print("Client: " + str(address))

    msg = 'Hello from server' + '\r\n'
    client.send(msg.encode('ascii'))
    client.close()