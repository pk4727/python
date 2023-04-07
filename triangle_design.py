n=int(input("enter the width:- "))
import math
for i in range(1,n):
    print((f"{i}".format(i))*i)
for i in range(1,n):
    print((pow(10, i)//9)*i)
    

for i in range(1,n):
    print(pow(int(("1")*i),2))
for i in range(1,n):
    print(pow((pow(10,i)//9),2))