from time import sleep
from turtle import *

# You can use the speed() function to speed up the drawing

bgcolor("black")
begin_fill()
color("orange")
circle(60)
end_fill()
penup()
forward(100)
pendown()
begin_fill()
color("gray")
circle(20)
end_fill()
penup()
forward(80)
pendown()
begin_fill()
color("red")
circle(40)
end_fill()
penup()
forward(90)
pendown()
begin_fill()
color("green")
circle(30)
end_fill()

sleep(5)