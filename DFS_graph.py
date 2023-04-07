import numpy
# n=numpy.array([[0,1,1,0,1,0,0],#0
#                [1,0,0,0,1,1,1],#1
#                [1,0,0,1,1,0,1],#2
#                [0,0,1,0,0,0,1],#3
#                [1,1,1,0,0,0,1],#4
#                [0,1,0,0,0,0,1],#5
#                [0,1,1,1,1,1,0]])#6 

m=int(input("Enter Total node in graph: "))                # 7
o=[]                                                                                                #(input matrix)
print("enter list with value '0' or '1' (number of value and list equal to total node):")           # 0 1 1 0 1 0 0
for i in range(m):                                                                                  # 1 0 0 0 1 1 1
    p=list(map(int,input().split()))                                                                # 1 0 0 1 1 0 1
    o.append(p)                                                                                     # 0 0 1 0 0 0 1                                                                           
n=numpy.array(o)                                                                                    # 1 1 1 0 0 0 1
#                                                                                                     # 0 1 0 0 0 0 1
#                                                                                                     # 0 1 1 1 1 1 0                                                                                                  
a=[]
b=(len(n[0]))                                                                                          
c=int(input("Enter source node: "))                                     #  1 or 7
f=[]
g=[]
a.append(c)
g.append(c)
for i in range(b):
    e=g[-1]
    # print("current stack element: ",g)
    # print("top value of stack:    ",e)
    g.pop(-1)
    # print("stack value after pop top element: ",g)
    # print("operation occur in top node:  \n")
    f.append(e)
    for j in range(b):
        d=n[e-1][j]
        if d==1:
            if j+1 not in a:
                g.append(j+1)
                a.append((j+1))
                

print("appending sequence in stack: ",a)
print("DFS sequence is: ",f)                                             # [1, 5, 7, 6, 4, 3, 2]  or  [7, 6, 5, 1, 4, 3, 2]
