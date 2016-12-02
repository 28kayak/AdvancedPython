#!/usr/bin/python3
__author__ = 'Kaya'

import socket


def mainf():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("Enter message: ")
    while message != 'q':
        #print(message.encode())
        encoded = message.encode()
        s.send(encoded)
        data = s.recv(1024)
        decoded = data.decode()
        print("Relieved from server: " + str(decoded))
        message = input()
    s.close()

if __name__ == '__main__':
    mainf()


