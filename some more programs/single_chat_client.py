import socket
c= socket.socket()
port= 1010
c.connect((socket.gethostname(),port))
print(c.recv(1024).decode())
