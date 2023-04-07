from itertools import combinations
n=list(input("enter veriable with (space) argument:- ").split())     # HACK 2
m=n[0]
o=int(n[1])
a=[]
for i in range(1,o+1):
    p=list(combinations(sorted(m),i))
    c=sorted(p)
    a.append(c)
for j in a:
    for k in j:
       print(''.join(k))
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK