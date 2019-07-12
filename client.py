import socket
import argparse

ADDR = 'localhost'
PORT = 7777

try:
    sock = socket.socket()
    sock.connect((ADDR, PORT))
    sock.send('Hi!'.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))


except KeyboardInterrupt:
    print('Serv socket closed. Good by!')