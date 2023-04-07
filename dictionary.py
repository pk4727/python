cities=["mumbai","new york","paris"]
state=["india","usa","france"]
q={city:states for city,states in zip(cities,state)}
print(q)
q=zip(cities,state)
for i in q:
    print(i)