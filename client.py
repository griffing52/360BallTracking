import socket
from threading import *

HOST = "127.0.0.1"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(HOST)
print(PORT)
s.bind((HOST, PORT))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b'Oi you sent something to me')

s.listen(5)
print('server started and listening')
while True:
    c, a = s.accept()
    client(c, a)