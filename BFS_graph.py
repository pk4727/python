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
                                                                                                    # 0 1 0 0 0 0 1
                                                                                                    # 0 1 1 1 1 1 0                                                                                                  
b=[]                                                                                              
d=int(input("Enter source node: "))                          #  1 or 7
b.append(d)
c=(len(n[0]))    #7
for i in range(c): 
    e=b[i]
    for j in range(c):
        p=(n[e-1][j])
        if p==1:
            if j+1 not in b:
                b.append(j+1)
print("BFS sequence is: ",b)                                                    # [1, 2, 3, 5, 6, 7, 4] or [7, 2, 3, 4, 5, 6, 1]


# b=[]
# d=int(input("Enter source node: "))
# b.append(d)
# c=(len(n[0]))    #7
# for i in b:
#     e=i
#     for i in range(c): 
#         for j in range(c):
#             p=(n[e-1][j])
#             if p==1:
#                 if j+1 not in b:
#                     b.append(j+1)
# print("BFS sequence is: ",b)
