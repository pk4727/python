from collections import Counter

# n=int(input("no of words and words:- "))
# # 4
# # bcdef
# # abcdefg
# # bcde
# # bcdef
# a=[]
# for i in range(n):
#     q=input()
#     a.append(q)
# print(Counter(a))
# print(len(Counter(a).items()))
# s=(Counter(a).values())
# print(*s)



# from collections import namedtuple

# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# dot_product = ( pt1.x * pt2.x ) + ( pt1.y * pt2.y )
# print(dot_product)
# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print(xyz.Class)


# n=int(input())    #5
# m=list(map(str,input().split()))   ## ID         MARKS      NAME       CLASS     
# l=[]
# for i in range(n):
#     p = list(map(str,input().split()))
#     l.append(p)
#     # 1          97         Raymond    7         
#     # 2          50         Steven     4         
#     # 3          91         Adrian     9         
#     # 4          72         Stewart    5         
#     # 5          80         Peter      6   
# a=0
# for i in range(len(m)):
#     if m[i]=="MARKS":
#         a=i
#     else:
#         pass
# average=0
# for i in l:
#     average=average+int(i[a])
# q=(average/n)
# print(round(q,2))    #78.00



# from collections import deque

# d = deque()
# d.append(1)
# print(d)
# deque([1])
# d.appendleft(2)
# print(d)
# deque([2, 1])
# d.clear()
# print(d)
# deque([])
# d.extend('1')
# print(d)
# deque(['1'])
# d.extendleft('234')
# print(d)
# deque(['4', '3', '2', '1'])
# d.count('1')
# 1
# d.pop()
# '1'
# print(d)
# deque(['4', '3', '2'])
# d.popleft()
# '4'
# print(d)
# deque(['3', '2'])
# d.extend('7896')
# print(d)
# deque(['3', '2', '7', '8', '9', '6'])
# d.remove('2')
# print(d)
# deque(['3', '7', '8', '9', '6'])
# d.reverse()
# print(d)
# deque(['6', '9', '8', '7', '3'])
# d.rotate(3)
# print(d)
# deque(['8', '7', '3', '6', '9'])


# n=int(input())   #6
# d=deque()
# for i in range(n):
#     p=(input().split())
#     # append 1
#     # append 2
#     # append 3
#     # appendleft 4
#     # pop
#     # popleft
#     if p[0]=="append":
#         d.append(int(p[1]))
#     elif p[0]=="appendleft":
#         d.appendleft(int(p[1]))
#     elif p[0]=="pop":
#         d.pop()
#     else:
#         d.popleft()
# print(*d)     #1 2



# from collections import OrderedDict

# ordinary_dictionary = {}
# ordinary_dictionary['a'] = 1
# ordinary_dictionary['b'] = 2
# ordinary_dictionary['c'] = 3
# ordinary_dictionary['d'] = 4
# ordinary_dictionary['e'] = 5
# print (ordinary_dictionary)
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# ordered_dictionary = OrderedDict()
# ordered_dictionary['a'] = 1
# ordered_dictionary['b'] = 2
# ordered_dictionary['c'] = 3
# ordered_dictionary['d'] = 4
# ordered_dictionary['e'] = 5
# print (ordered_dictionary)


# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
# d={}
# n=int(input())   #9
# for i in range(n):
#     item, price = input().rsplit(maxsplit=1)
# # BANANA FRIES 12
# # POTATO CHIPS 30
# # APPLE JUICE 10
# # CANDY 5
# # APPLE JUICE 10
# # CANDY 5
# # CANDY 5
# # CANDY 5
# # POTATO CHIPS 30
#     d[item] = d.setdefault(item, 0) + int(price)
# p=(f'{k} {v} ' for k, v in d.items())
# print('\n'.join(p))
# # BANANA FRIES 12
# # POTATO CHIPS 60
# # APPLE JUICE 20
# # CANDY 20
