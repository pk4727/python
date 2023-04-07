#if the sum of digits of given number is factor of the number then the number is harshad number
#eg=21,156,153,200,175

n=input("enter the no: ")       #156 harshad number or not
a=0
for i in n:
    a+=int(i)
print(a)

if int(n)%a==0:
    print(True)
else:
    print(False)                #true