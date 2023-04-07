class personA:
    def __init__(self,name,village,distric,state):
        self.name=name
        self.village=village
        self.distric=distric
        self.state=state
    def showA(self):
        print("personA name: ",self.name)
        print("personA village: ",self.village)
        print("personA distric: ",self.distric)
        print("personA state: ",self.state)
class personB(personA):
    def __init__(self,name,village,distric,state,father,mother):
        super().__init__ (name,village,distric,state)
        self.father=father
        self.mother=mother
    def showB(self):
        print("father's name: ",self.father)
        print("mother's name: ",self.mother)
class personC(personB):
    def __init__(self,name,village,distric,state,father,mother,brother,sister):
        super().__init__(name,village,distric,state,father,mother)
        self.brother=brother
        self.sister=sister
    def showC(self):
        print("brother is: ",self.brother)
        print("sister is: ",self.sister)
##objA=personA("pk","pindatand","giridih","jharkhand")
##objA.showA()
##objB=personB("khirodhar mahto","sumitra devi")
##objB.showB()
objC=personC("pk","pindatand","giridih","jharkhand","khirodhar mahto","sumitra devi","deepak kr","sangita devi")
objC.showA()
objC.showB()
objC.showC()