def crc(generator,message):
    g= len(generator)
    message= message.ljust(g-1 + len(message),'0')
    print(message)
    m= len(message)
    temp= message[:g-1]
    i= g-1
    while(i<m):
        if temp[0]=='1':
            temp= temp^g
            i+= 1
        else:
            temp+= message[i+1]


crc("1101","100100")
    