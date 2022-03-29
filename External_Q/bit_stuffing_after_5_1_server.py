# binary string to server and server returns the string after
#  bit-stuffing (After every 5 consecutive 1s insert a 0)
def bit_stuffing(str1):
    check= ""
    temp= str1
    print(temp)
    count=0 # to count if already one set of '11111' has came or not
    for i in range(len(str1)):
        if str1[i]=='1':
            check+= str1[i]   # add in check
        if str1[i]=='0':  # if true then maek check= null
            check= ""
        if check=='11111':  # append '0' if it is equal to '11111'
            temp= temp[:(i+count+1)] + "0" + temp[(count+i+1):]
            count+= 1   # incr the count
            check= ""
    return temp

str1= input("enter any string of 0 and 1: ")
print(bit_stuffing(str1))
