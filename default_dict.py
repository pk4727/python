from collections import defaultdict
d=defaultdict(list)
e=defaultdict(list)
d['group A'].append("a")
d['group A'].append("a")
d['group A'].append("b")
d['group A'].append("a")
d['group A'].append("b")
e['group B'].append("a")
e['group B'].append("b")
print(d.items())
print(e.items())


# from collections import defaultdict
# m,n=map(int,input().split())
# d=defaultdict(list)
# for i in range(m):
#     p=input().strip()
#     d[p].append(i+1)
# for j in range(n):
#     p=input().strip()
#     if p in d:
#         print(' '.join(map(str,(d[p]))))
#     else:
#         print(-1)