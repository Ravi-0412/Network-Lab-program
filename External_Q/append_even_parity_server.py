# def even_parity(n):
#     # to count the no of 1's we have to get the last bit
#     count=0
#     temp= n
#     while(n>0):
#         if n & 1==1:
#             count+= 1
#         n>>= 1
#     print(count)
#     if count%2==1:
#         return 2*temp+1   # appending '1' at last in binary is =2*n+1
#     else:
#         return 2*temp       #appending '0' at last in binary is =2*n

# n= int(input("enter the number: "))
# print(even_parity(n))


# or
def even_parity(n):
    # to count the no of 1's we have to get the last bit
    count=0 
    temp= n
    # no of times this loop will execute that will give
    # the no of '1'
    while(n>0):
        n= n & n-1
        count+= 1
    if count%2==1:
        return 2*temp+1   # appending '1' at last in binary is =2*n+1
    else:
        return 2*temp       #appending '0' at last in binary is =2*n

n= int(input("enter the number: "))
print(even_parity(n))

