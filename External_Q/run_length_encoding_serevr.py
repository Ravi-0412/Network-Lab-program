# only valid if ele doen't repeat later again 
# once any distinct later comes after that ele

from collections import Counter
def run_length(str1):
    encoding= ""
    freq= Counter(str1)  # will store the count of each ele in a dictionary
    for ele in freq:
        # print(ele,freq[ele],end="")  
        # print('{}{}'.format(ele,freq[ele]))
        encoding+= ele + str(freq[ele])
    print(encoding)
str1= input("enter any combination of a b c d: ")
run_length(str1)


# general one

# def run_length(str1):
#     check= []
#     count= 0
#     encode= ""
#     for i in range(len(str1)):
#         if not check:   # if check is empty
#             check.append(str1[i])
#             count+= 1
#         else:   # if check is not empty,comapre the elements in both
#             if check[-1]== str1[i]:
#                 check.append(str1[i])
#                 count+= 1
#             else:  # if top of check is not equal to the str[i]
#                     # print or store the val of check and count
#                 encode+= check[-1] + str(count)
#                 # now make the check empty and count=0
#                 check, count= [], 0
#                 # again append the str[i] into check and again incr the count
#                 check.append(str1[i])
#                 count+= 1
#     # for combination of char at last there is nothing to comapre 
#     # and store in result. 
#     # so add the last remaining char with their count
#     encode+= check[-1] + str(count)  
#     return encode

# str1= input("enter any combination of string: ")
# print(run_length(str1))






            