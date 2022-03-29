import socket
c=socket.socket()
port=7888
c.connect((socket.gethostname(),port))
c.send(input("enter the number").encode())
msg1=c.recv(1024).decode()
print(msg1)
msg2=c.recv(1024).decode()
print(msg2)
c.close()
