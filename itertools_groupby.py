import itertools
a=input("enter the word:- ")
b=[]
p=itertools.groupby(a)
p=[list(g) for k,g in p]
for i in p:
    q=(len(i),(i[0]))
#     b.append(q)
# print(*b)
    print(q)