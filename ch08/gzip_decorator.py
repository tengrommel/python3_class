import socket
import gzip
from io import BytesIO

class GzipSocket:
    def __init__(self):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()


def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(GzipSocket(client))
finally:
    server.close()