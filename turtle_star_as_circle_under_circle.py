import turtle
import colorsys
t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.speed(1000)
n=36
m=0
print("done")
for i in range(100):
    c=colorsys.hsv_to_rgb(m,1,0.9)
    m+=1/n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(300)
        t.left(150) 