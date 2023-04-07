import numpy

m,n=map(int,input().split()) # 4 2
o=[]
for i in range(m):
    p=list(map(int,input().split()))
    # 2 5
    # 3 7
    # 1 3
    # 4 0
    o.append(p)
array=numpy.array(o)
p=(numpy.min(array,axis=1))
print(numpy.max(p,axis=None))


# n=int(input())   # 2         0.0
# a=[]
# for i in range(n):
#     e=list(map(eval,input().split()))
#     # 1.1 1.1
#     # 1.1 1.2
#     a.append(e)
# numpy.set_printoptions(legacy='1.13')
# print(numpy.linalg.det(a))


# # 0 1     3  [[0 0]  [2 3]]
# # 2 3
# a1=numpy.array(list(map(int,input().split())))
# a2=numpy.array(list(map(int,input().split())))
# print(numpy.inner(a1,a2))
# print(numpy.outer(a1,a2))


# # 1.1 2 3        3.0
# # 0
# c=list(map(float,input().split()))
# x=int(input())
# print(numpy.polyval(c,x))


# # 2                  [[ 7 10][15 22]]
# # 1 2
# # 3 4
# # 1 2
# # 3 4
# n=int(input())
# a1=[]
# a2=[]
# for i in range(n):
#     c1=list(map(int,input().split()))
#     a1.append(c1)
# for i in range(n):
#     c2=list(map(int,input().split()))
#     a2.append(c2)
# print(numpy.dot(a1,a2))
# print(numpy.cross(a1,a2))    #[0 0]


# # 2 2    [ 1.5  3.5] [ 1.  1.] 1.11803398875
# # 1 2
# # 3 4
# n,m=map(int,input().split())
# a=[]
# for i in range(n):
#     p=list(map(int,input().split()))
#     a.append(p)
# print(numpy.mean(a,axis=1))
# print(numpy.var(a,axis=0))
# print(round(numpy.std(a,axis=None),11))


# # 2 2       24
# # 1 2
# # 3 4
# n,m=map(int,input().split())
# a=[]
# for i in range(n):
#     p=list(map(int,input().split()))
#     a.append(p)
# p=numpy.sum(a,axis=0)
# print(numpy.prod(p))


# # 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
# #        [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# #        [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# #        [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
# a=list(map(eval,input().split()))
# numpy.set_printoptions(legacy='1.13')
# print(numpy.floor(a))
# print(numpy.ceil(a))
# print(numpy.rint(a))


# # 1 4       [[ 6  8 10 12]]
# #           [[-4 -4 -4 -4]]
# #           [[ 5 12 21 32]]
# #           [[0 0 0 0]]
# #           [[1 2 3 4]]
# #           [[    1    64  2187 65536]] 
# # 1 2 3 4
# # 5 6 7 8
# m,n=map(int,input().split())
# c1=[]
# c2=[]
# for i in range(m):
#     a1=list(map(eval,input().split()))
#     c1.append(a1)
# for i in range(m):
#     a2=list(map(eval,input().split()))
#     c2.append(a2)
# print("{}".format(numpy.add(c1,c2)))
# print("{}".format(numpy.subtract(c1,c2)))
# print("{}".format(numpy.multiply(c1,c2)))
# print("{}".format(numpy.floor_divide(c1,c2)))
# print("{}".format(numpy.mod(c1,c2)))
# print("{}".format(numpy.power(c1,c2)))


# # 3 3   [[ 1.  0.  0.][ 0.  1.  0.][ 0.  0.  1.]]
# rows,column=map(int,input().split())
# numpy.set_printoptions(legacy='1.13')
# print( numpy.eye(rows,column,k=0))
# print(numpy.eye(rows,column,k=-1))
# print(numpy.identity(rows))
# print(numpy.identity(column))


# # 4 3 2       [[1 2][1 2][1 2][1 2][3 4][3 4][3 4]] 
# # 1 2
# # 1 2 
# # 1 2
# # 1 2
# # 3 4
# # 3 4
# # 3 4 
# n,m,p=input().split()
# a1=[]
# a2=[]
# for i  in range(int(n)):
#     p=list(map(int,input().split()))
#     a1.append(p)
# for j  in range(int(m)):
#     p=list(map(int,input().split()))
#     a2.append(p)
# arr=numpy.array(a1)
# arrr=numpy.array(a2)
# print(numpy.concatenate((arr,arrr),axis=0))


# # 2 2     [[1 3][2 4]][1 2 3 4]
# # 1 2
# # 3 4
# n,m=input().split()
# a=[]
# for i in range(int(n)):
#     p=list(map(int,input().split()))
#     a.append(p)
# arr=numpy.array(a)
# print(numpy.transpose(arr))
# print(arr.flatten())


# # 1 2 3 4 5 6 7 8 9    [[1 2 3][4 5 6][7 8 9]]
# p=list(map(int,input().split()))
# arr=numpy.array(p)
# print(numpy.reshape(arr,(3,3)))


# # 1 2 3 4 -8 -10  [-10.  -8.   4.   3.   2.   1.]
# def arrays(arr):
#     arr.reverse()
#     return numpy.array(arr,float)
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)
