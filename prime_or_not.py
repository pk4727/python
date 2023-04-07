# flag=0  
# n=int(input("enter the number you want to check"))
# i=2
# while i<=(n/2):
#     if(n%i)==0:
#       flag=1
#       break
#     else:
#         i+=1
# if(n==1):
#     print(n,"is neither prime or composite")
# elif(flag==1):
#     print(n,"is not prime number")
# elif(flag==0):
#     print(n,"is prime number")
    

def prime(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    if len(l)==2:
        print("no is prime")
    else:
        print("no is not prime")
m=int(input("enter the no you want to check"))
prime(m)

        