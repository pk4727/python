# import itertools
# def perm(p,l):
#     print(list(itertools.permutations(p,l)))
# def comb(p,l):
#     print(list(itertools.combinations(p,l)))
# n=list(map(int,input("list of numbers space separated").split()))
# m=int(input("enter the width"))
# perm(n,m)
# comb(n,m)



from math import factorial as fact
def permutation(n, r):
    """Returns the number of permutations of n items taken r at a time"""
    return fact(n) // fact(n-r)

def combination(n, r):
    """Returns the number of combinations of n items taken r at a time"""
    return fact(n) // (fact(r) * fact(n-r))

n=int(input("Enter the no n:\t"))
r=int(input("Enter the no r:\t"))
print("\npermutation is: ",permutation(n,r))
print("\ncombination is: ",combination(n,r))





