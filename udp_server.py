from datetime import datetime
import socket

server_address = ('localhost',6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data,client = server.recvfrom(max_size)
i = data.decode('utf-8')
print('At', datetime.now(), client, 'said', i)
server.sendto(b'Are you talking to me?', client)
server.close()