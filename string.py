# n=['Anil','Amal','Aditya','Avi','Alka']
# print(n)
# n.insert(2,"Anuj")
# print(n)
# n.append('Zulu')
# print(n)
# i=n.index('Anil')
# n[i]=('Anil Kumar')
# print(n)
# n.sort()
# print(n)
# n.reverse()
# print(n)
# n.remove('Avi')
# print(n)


# t7=("A","B","C","D","E","F")
# print(t7[2:5])
# print(t7[3:])
# print(t7[:5])
# print(t7[-4:-1])
# print(t7[-4:])


def merge_the_tools(string, k):
    m=[]
    for i in range(0,len(string),3):
        p=string[i:i+k:]
        m.append(p)
    print(m)
    for i in m:
        pass
if __name__ == '__main__':
    string, k = "AABCAAADA",3
    merge_the_tools(string, k)          #AB CA AD


