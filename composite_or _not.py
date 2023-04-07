flag=0  
n=int(input("enter the number you want to check"))
i=2
while i<=(n/2):
    if(n%i)==0:
      flag=1
      break
    else:
        i+=1
if(n==1):
    print(n,"is neither prime or composite")
elif(flag==1):
    print(n,"is composite number")
elif(flag==0):
    print(n,"is not composite number") 