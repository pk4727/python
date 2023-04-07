n=3    #no of element in set s happiness(if a[i] foun in s then +1 and if b[i] found in s then -1)
m=2    # no of element in set a=happiness set(+1),b=happinness set(-1)
s=(1,5,3)
a=(3,1)
b=(5,7)
p=0
for i in range(0,len(s)):
   for j in range(0,len(a)):
     if(s[i]==a[j]):
         p+=1
   for k in range(0,len(b)):
     if(s[i]==b[k]):
         p-=1
print(p)