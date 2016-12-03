#!/usr/bin/python3
__author__ = 'kaya'
import socket


def mainf():
    localhost = '127.0.0.1'  # localhost
    host = "172.31.23.155"
    port = 5000
    numOfsocket = 1  # number of socket to be listened

    s = socket.socket()  # create socket instance
    s.bind((host, port))
    print("Server is now listening....")
    s.listen(numOfsocket)
    c, addr = s.accept()

    print("Connection from " + str(addr))
    while True:
        data = c.recv(1024)

        if not data:
            break
        decoded = data.decode()
        print("From connected user: " + str(decoded))
        data = str(decoded).upper()  # capitalize sent data from user

        encoded = data.encode()
        print("Sending: " + str(encoded))
        c.send(encoded)
    c.close()

if __name__ == '__main__':
    mainf()
# $ ps -fA | grep python to find out process ID running this program
