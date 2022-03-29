
def run_length(str1):
    ans=""
    ans+= str1[0] + ","  # add 1st char as it is 
    for i in range(1,len(str1)):
        temp= int(str1[i]) - int(str1[i-1])
        if i==len(str1)-1:      # to avoid comma at last      
            if temp>=0:
                ans+= "+" + str(temp)
            if temp<0:
                ans+= str(temp)
        else:
            if temp>=0:
                ans+= "+" + str(temp) + ","
            if temp<0:
                ans+= str(temp) + ","
    return ans

import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port= 4567
s.bind((socket.gethostname(),port))

while True:
    data,addr= s.recvfrom(4096)
    print(data.decode())
    message= "welcome to the UDP server!".encode()
    s.sendto(message,addr)
    data,addr= s.recvfrom(4096)
    number= data.decode()
    print(number)
    ans= str(run_length(number)).encode()
    s.sendto(ans,addr)