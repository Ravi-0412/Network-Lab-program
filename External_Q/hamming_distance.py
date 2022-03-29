
# n1 = int(input("phele number dalo 0 1 ke form me"),2)
# n2 = int(input("dusra number dalo ye bhiu 0 1 ke form me"),2)
# res = bin(n1^n2).replace("0b","")
# print(res.count('1'))
def binarytodecimal(n):
    l=len(n)
    res=n[: : -1]
    result=0
    for i in range(l):
        result+=int(res[i])*pow(2,i)
    return result

def decimaltobinary(n):
    if(n<2):
        return str(n)
    ans = decimaltobinary(n//2)
    return ans + str(n%2)

n1 = input("phele number dalo 0 1 ke form me")
n2 = input("phele number dalo 0 1 ke form me")
dec_n1=binarytodecimal(n1)
dec_n2=binarytodecimal(n2)

res_dec=dec_n1^dec_n2
res_bin= decimaltobinary(res_dec)
count=0
for i in res_bin:
    if(i=='1'):
        count+=1
print("hamming distance= ",count)


