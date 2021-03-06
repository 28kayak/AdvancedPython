#!/usr/bin/python3
__author__ = 'Kaya'

import socket


def mainf():
    s = socket.socket() # create socket instance
    localhost = '127.0.0.1'
    #host = '172.31.23.155'
    host = socket.gethostname(socket.AF_INET, socket.SOCK_STREAM)
    print("Host Name: " + str(host))
    port = 5000

    print("Connecting to the server.......")
    s.connect((host, port))
    print("Server is connected")
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


