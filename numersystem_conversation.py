import math
n=int(input("enter the no you want to change from decimal:-"))
print("1.Binary")
print("2.octal")
print("3.hexadecimal")
m=int(input("your choose:-"))
if m==1:
    p=(bin(n))
    print(p[2:])
elif m==2:
    p=(oct(n))
    print(p[2:])
elif m==3:
    p=(hex(n))
    print(p[2:])
else:
    print("invilid choose")



# roman