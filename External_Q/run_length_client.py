import socket
c= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port= 4567
ip= socket.gethostname()
message= "hello udp server!".encode()
c.sendto(message,(ip,port))
data,addr= c.recvfrom(4096)
print(data.decode())
number= (input("enter the number: ")).encode()

c.sendto(number,(ip,port))
print("relative encoding is: ")
data,addr= c.recvfrom(4096)
print(data.decode())
c.close()
