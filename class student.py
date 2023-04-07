class student:
    def __init__(self,name,roll,stream):
        self.n=name
        self.r=roll
        self.s=stream
    def show(self):
        print("name of student: ",self.n)
        print("roll no of student: ",self.r)
        print("stream of student: ",self.s) 
obj=student("pk",87,"cse(ai&ml)")
obj.show()