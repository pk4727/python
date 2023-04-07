import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for j in range(35):
    for i in range(25):
        tur.color(cs.hsv_to_rgb(i/25,j/35,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.left(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done()