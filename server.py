import socket
import argparse


ADDR = 'localhost'
PORT = 7777

try:
    serv_sock = socket.socket()
    serv_sock.bind((ADDR, PORT))
    serv_sock.listen(5)
    while True:
        sock, addr = serv_sock.accept()
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        sock.send('OK'.encode('utf-8'))
        sock.close()


except KeyboardInterrupt:
    print('Serv socket closed. Good by!')
