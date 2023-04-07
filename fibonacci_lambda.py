# cube = lambda x: x**3
# def fibonacci(n):
#     list = []
#     for i in range(n):
#         if(i == 0):
#             x = 0
#             list.append(x)
#         elif(i == 1):
#             x = 1
#             list.append(x)
#         else:
#             x = list[i - 1] + list[i - 2]
#             list.append(x)
#     return list
# if __name__ == '__main__':
#    n = int(input("enter the number: "))
#    print("fibonacci series is: ",fibonacci(n))
#    print("cube of fibonacci series is: ",list(map(cube, fibonacci(n))))
   
   
# def fibonacci(n):                                          #fibonacci series
#     list = []
#     for i in range(n):
#         if(i == 0):
#             x = 0
#             list.append(x)
#         elif(i == 1):
#             x = 1
#             list.append(x)
#         else:
#             x = list[i-1] + list[i-2]
#             list.append(x)
#     return list
# n = int(input("enter the number: "))
# print(fibonacci(n))


def febo(n):                               #reccursion method
    if n<=1:
        return n
    else:
        return (febo(n-1)+febo(n-2))
n=int(input("enter the no of terms:"))
for i in range(n):
    print(febo(i))