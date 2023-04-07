# # choose an element from all list such that the square ofremainder is greater 
# # (you can choose any of the element form list either max or min)
# # 3 1000   (no of list and divisor for remainder)
# # 2 5 4
# # 3 7 8 9 
# # 5 5 7 8 9 10 

# import itertools

# NUMBER_OF_LISTS, MODULUS = map(int, input().split())
# LISTS_OF_LISTS = []

# for i in range(0, NUMBER_OF_LISTS):
#     new_list = list(map(int, input().split()))
#     del new_list[0]
#     LISTS_OF_LISTS.append(new_list)

# def squared(element):
#     return element**2

# COMBS = list(itertools.product(*LISTS_OF_LISTS))
# RESULTS = []

# for i in COMBS:
#     result1 = sum(map(squared, [a for a in i]))
#     result2 = result1 % MODULUS
#     RESULTS.append(result2)

# print(max(RESULTS))                #206

# #or

import itertools
n=3
m=1000
l1={2,5,4}
l2=[3,7,8,9]
l3=[5,5,7,8,9,10]
p=list(itertools.product(l1,l2,l3))
print((p))
q=0
for i in p:
    r=0
    for j in i:
        r+=pow(j,2)
    if r>q:
        q=r
    r=0
print(q)