import socket
c= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip= socket.gethostname()
port= 55550
msg= "hello UDP server!".encode()
c.sendto(msg,(ip,port))
data, addr= c.recvfrom(4096)
print("server says")
print(str(data))
c.close()
