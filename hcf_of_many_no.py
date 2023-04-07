n=int(input("HCF of how many no.(enter):-"))
a=[]
for i in range (n):
    m=int(input("input number: "))
    b=[]
    for j in range (1,m+1):
        if (m%j)==0:
            b.append(j)
    a.append(set(b))
    b=[]
# print(a)
c=a[0]
for k in range(1,len(a)):
    p=(c&(a[k]))               #comman chek in corresponding set of a
    c=set(p)
# print(p)
d=1   
for i in p:
    d=d*i
print("HCF is ",d)


import math
n=int(input("HCF of how many no.(enter):-"))
a=int(input("Enter number"))
for i in range (n-1):
    m=int(input("Enter number:"))
    p=math.gcd(a,m)
    a=p
print("HCF is",a)

