class Solution:
    def MissingNumber(self,array,n):
        
        
        # a=0
        # for i in range(1,n+1):
        #     if i not in array:
        #         a=i
        # return a
    
        m=int((n*(n+1))/2)
        o=0
        for i in array:
            o=o+i
        return m-o
t=1
for _ in range(0,t):
    n=int(input("enter the len of array"))
    a=list(map(int,input("enter the array").split()))
    s=Solution().MissingNumber(a,n)
    print(s)