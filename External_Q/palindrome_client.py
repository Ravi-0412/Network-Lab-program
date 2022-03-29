import socket
c=socket.socket()
port=7888
c.connect((socket.gethostname(),port))
c.send(input("enter the string").encode())
msg=c.recv(1024).decode()
print(msg)
c.close()
