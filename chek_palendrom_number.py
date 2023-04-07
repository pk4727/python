 ## palindrom number is a type of number in which when we read the digit from right side is  
 ## equal to the number when read the digit from left side.eg-> 121,12321,123321,14541,etc.
 
n=int(input("enter the number you want to check"))
temp=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(temp==r):
    print("palendrom")
else:
    print("not palendrom")