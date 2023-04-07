import turtle
import colorsys
from turtle import *
color('red', 'yellow')
begin_fill()
speed(100)
print("done")
while True:
    forward(250)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()