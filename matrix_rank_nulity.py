from sympy import Matrix
 
row1=[1,-3,0,-3,-1]   # [1,4,5,2]
row2=[-1,4,0,6,4]    #  [2,1,3,0]
row3=[-1,3,0,3,2]    #   [-1,3,2,2]
A = [row1,row2,row3]
A = Matrix(A)
# Number of Columns
NoC = A.shape[1]
# Rank of A
rank = A.rank()
# Nullity of the Matrix
nullity = NoC - rank
print("no. of column :", NoC)
print("rank :", rank)
print("Nullity :", nullity)