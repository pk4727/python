## An armstrong number is number in which the sum of all digits with power(power=no. of digit)  
## gives the number itself eg ->0,1,153=(1^3+5^3+3^3),370=(3^3+7^3+0^3),371=(3^3+7^3+1^3),
## 407=(4^3+0^3+7^3),1634=(1^4+6^4+3^4+4^4),8280=(8^4+2^4+8^4+0^4),9474=(9^4+4^4+7^4+4^4),etc.

def cube(x,p):
    f=pow(x,p)
    return f
s=input("enter a number")
l=len(s)
n=int(s)
c=n
r=0
while c>0:
    d=c%10
    r=r+cube(d,l)
    c=c//10
if(n==r):
    print(n,"is armstrong no")
else:
    print(n,"is not armstrong no")