# # company logo
# # Here, b occurs  times. It is printed first.
# # Both a and c occur  times. So, a is printed in the second line and 
# # c in the third line because a comes before c in the alphabet.


# from collections import Counter
# s = input()                                     #aabbbccde
# l = sorted(list(s))
# c = Counter(l)
# mc = c.most_common(3)
# for a,b in mc:
#     print(f'{a} {b}')                           # b 3 a 2 c 2

# #or

from collections import Counter
s="aabbbccde"
c=Counter(s)
common=c.most_common(3)
for i,j in common:
    print(i,j)
print(c)