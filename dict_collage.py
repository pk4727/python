d={
    "Pradhuman":431022110087,
    "Sayantan":431022110085
}
# d["abir"]=431022110086                         #add item in dict
# d.update({"Oniman":431022110089})              #update item in dict
# print(d) 
  

e={
    "Pradhuman":" verma",
    "Abir":" nath",
    "Sayantan":" laha",
    "Oniman":" kumar"
}     
# print(e)


# q={}
# q.update(d)
# q.update(e)
# print(q)                                   # concate two dict

                    
f={
    "Pradhuman":"kumar",
    "Sayantan":"kumar"
}


# n=input("enter the key you want to check in dict. ")
# if n in e:                                           #check key is present in dict
#     print(True)
# else:
#     print(False)

# print(q.items())                          #all items of dict
# print(q.values())                         #all values of dict


# s=sum(d.values())                          #sum all values of dict
# print("sum of values is",s) 


# r=max(d.values())
# s=min(d.values())
# print("maximum no of dictonary values is",r)                                    # max of dict values
# print("minimum no of dictonary values is",s)                                    # min of dict values



# l1=["collage","state","distic","area"]
# l2=["narula institute of technplogy","west bengal","24 north prangana","agarpara"]
# c=dict(zip(l1,l2))
# print(c)

# or

# a={}
# b=0
# for i in l1:
#     for j in range(b,len(l2)):
#         a.update({i:l2[j]})
#         b+=1
#         break;
# print(a.items())                                         #list to dictionary conversion



# e={'b': 20, 'c': 50, 'a': "10" }
# f={'ab': 200, 'bc': 500, 'a': "100","b":10}
# for k in e:
#     if k in f:
#         f[k] += e[k]
#     else:
#         f[k] = e[k]    
# print(f)                                                #adding of value having same key in two dic



# a=["a","b","c","c"]
# b=[10,20,40,50]
# d=dict(zip(a,b))
# c=set(d.items())      
# g=dict(c)
# print(g)              #(dict cant take duplicate key)but remove duplicate key in dict in this way also





import itertools

m = {
    "pk": "a",
    "ak": "s",
    "sk": "p"
}
combinations = itertools.product(("pk"),("ak"),("sk"))
for combination in combinations:
    print("".join(combination))
    
    