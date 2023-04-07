import math
from turtle import*
import colorsys
bgcolor('black')
tracer(50)
pensize(3)
def drawShape():
    up()
    goto(-65,45)
    down()
    h=0
    for i in range(550):
        myColor=colorsys.hsv_to_rgb(h,1,1)
        h+=0.0035
        color('black')
        fillcolor(myColor)
        begin_fill()
        fd(26)
        lt(54)
        circle(i/2,80,steps=5)
        end_fill()
        bk(85)
        color('white')
        rt(99)
        bk(75)
        circle(i,42,steps=3)
print("Done")        
drawShape()  
done()     