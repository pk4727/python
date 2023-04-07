## krishnamurti number is number in which sum of factorial of each degits is equal to the
## number itself.eg->2=(2!=2),154=(i!+4!+5!=1+24+120=145).

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        return f
n=int(input("enter a number"))
c=n
r=0
while c>0:
    d=c%10
    r=r+fact(d)
    c=c//10
if(n==r):
    print(n,"is krishnamurti number")
else:
    print(n,"is not krishnamurti number")