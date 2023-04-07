import math
n=int(input("enter the depth of the door mate:-"))
m=3*n
for i in range(0,math.floor(n/2)+1):
    print((".|."*((2*i)+1)).center(m,'-'))
print((": P.K :").center(m,'-'))
for i in range((math.floor(n/2)+1),0,-1):
    print((".|."*((2*i)-1)).center(m,'-'))