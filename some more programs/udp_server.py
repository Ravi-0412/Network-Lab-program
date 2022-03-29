import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 1st para tells
# it is of IPV4 family and 2nd para tells that it is a UDP conection
port= 55550
s.bind((socket.gethostname(),port))
# after binding data exchange can take place, no need to establish the connection

while True:
    data, addr= s.recvfrom(4096) # recvfrom() returns two things data & addr in udp
    print(str(data))
    message= "hello I am a UDP server!".encode()
    # msg= "hello I am a UDP server!"
    # message= bytes(msg,encoding='utf-8')
    s.sendto(message, addr)
    
