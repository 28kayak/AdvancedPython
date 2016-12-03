# UDP: User Datagram Protocol

UDP is a UN-reliable connection-LESS based protocol. 
Low overhead. if data loss while transferring, then loose forever. 
But, in trade off, it is fast to communicate to other device.

It is used for: 

  - VOIP 
  - Online Games
  - Streaming
Go on a terminal for a server-side:
```sh
$ python3 udpServer.py
```
Go to the other terminal that represents a client 
```sh
$python3 udpClient.py
```