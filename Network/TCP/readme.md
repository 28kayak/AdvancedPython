# TCP: transmission control protocol

TCP is a reliable connection based protocol. 
It is ordered and checks an error( by simplely chacked sum)
But, in trade off, it is slow to communicate to other device.

It is used for: 

  - Web browsers 
  - Email 
  - SSH (Secure SHell)
  - FTP(i.e. file transfer protocol) 
  - etc 

*ssh is cryptographic network protocol for operating network services securely over an unsecured network. 


Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ npm run predeploy
$ NODE_ENV=production node app
```





