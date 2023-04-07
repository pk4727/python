# import math                             #logic
# a=[5,10,15,20]
# b=math.gcd(a[0],a[1])
# c=a[0]*a[1]
# d=int(c/b)
# print(d)
# e=math.gcd(d,a[2])
# f=d*a[2]
# g=int(f/e)
# print(g)
# h=math.gcd(g,a[3])
# i=g*a[3]
# j=int(i/h)
# print("lcm is ",j)


import math
a=int(input("Enter how many number are input for LCM : "))             #implied logic
lcm=int(input("enter number "))
for i in range(a-1):
    print("LCM of input number till now=",lcm)
    d=int(input("enter number "))
    hcf=math.gcd(lcm,d)
    product=lcm*d
    lcm=int(product/hcf)

print("final LCM of input numbers=",lcm)


# print("enter four number for LCM calculation")                       #without inbild function
# e=int(input("enter no:"))
# f=int(input("enter no:"))
# g=int(input("enter no:"))
# h=int(input("enter no:"))
# def lcm(a, b, c, d):
#     max_num = max(a, b, c, d)
#     i = 1
#     while True:
#         multiple = max_num * i
#         if multiple % a == 0 and multiple % b == 0 and multiple % c == 0 and multiple % d == 0:
#             return multiple
#         i += 1
# result = lcm(e,f,g,h)
# print(result)                               # Output: 72