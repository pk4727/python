print (list(map(len, ['Tina', 'Raj', 'Tom'])))     # [4, 3, 3]  



sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))    # 6


cube=lambda x:x**3
print(cube(2))     # 8


def fun(n):
    return [1,2,3,4]
__name__=="__main__"
n=5
print(list(map(cube,fun(n))))  # [1, 8, 27, 64]