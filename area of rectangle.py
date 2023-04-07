n=int(input("length"))
m=int(input("breadth"))
class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def showlb(self):
        print("length of rectangle:",self.l)
        print("breadth of rectangle:",self.b)
        print("area of rectangle:",(self.l*self.b))
obj=rectangle(n,m)
obj.showlb()