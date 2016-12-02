# TCP: transmission control protocol

TCP is a reliable connection based protocol. 
It is ordered and checks an error( by simply checked sum)
But, in trade off, it is slow to communicate to other device.

It is used for: 

  - Web browsers 
  - Email 
  - SSH (Secure SHell)
  - FTP(i.e. file transfer protocol) 
  - etc 

*ssh is cryptographic network protocol for operating network services securely over an unsecured network. 




```sh
$ python3 tcpServer.py
```
Go to the other terminal that represents a client 
'''sh 
$python3 tcpClient.py
'''

#socket.error: [Errno 48] Address already in use
while you are testing, you might face to this error. Then do as the followings: 
'''sh 
$ ps -fA | grep python
  501 80950 58051   0 10:15PM ttys010    0:00.00 grep python
  
$ kill 58051  
'''
After killing, run as it is. 





