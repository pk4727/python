n=int(input("enter th value of width:- "))

# for upeer  triangle
for i in range(n+2):
    print("* "*(i))
print("* "*(n+2))
for i in range(1,n+1):
   print("*"," "*(n+(n-1)),"*","* "*i)
   
# for middle line or section line of space
print("* "*((n*2)+3))

# for lower triangle
for i in range(1,n+1):
   print("*"," "*(n+(n-1)),"*","* "*((n+1)-i))
for j in range(n+2):
    print("* "*((n+2)-j))