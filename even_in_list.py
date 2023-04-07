def even(l):
    for i in l:
        if i%2==0:
            print(i)
l=list(map(int,input("enter the element of list space separated").split()))
even(l)