# n=int(input())      #3 no of condition  
# for i in range(n):
#     m,o=list(map(str,input().split()))            #no of element in series a/c to the input say  
#     # odd 2                                                   #if odd 2 then print 2 odd no from 0
#     # even 3                                                  #if even 2 then print 2 even no from 0
#     # odd 5
#     a="odd"
#     b="even"
#     if(m==a):
#         for i in range(1,2*int(o)):
#             if(i%2!=0):
#                 print(i)
#     elif(m==b):
#         for i in range(0,2*int(o)):
#             if(i%2==0):
#                 print(i)
# # 1
# # 3
# # 0
# # 2
# # 4
# # 1
# # 3
# # 5
# # 7
# # 9

# #---------------------------------------------------------------------------------------------------------------------------

# m=(input("enter the string: ").split())    #word score if even then 2 else 1 for no of even in string
# n="aeiouy"
# a,d=0,0
# b=[]
# e=[]
# for i in m:
#     for j in i:
#         if j not in n:
#             d+=1
#         else:
#             a+=1
#     b.append(a)
#     a=0
#     e.append(d)
#     d=0
# print(b)
# print(e)
# c=0
# f=0
# for i in b:
#     if i%2==0:
#         c+=2
#         f+=2
#     else:
#         c+=1
#         f+=1
# print(c)
# print(f)