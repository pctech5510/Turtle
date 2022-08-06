from turtle import *
import turtle

diameter = 40
pop_diameter = 100

def draw_balloon():
    color("red")
    dot(diameter)


def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()
    if diameter == pop_diameter:
        clear()
        diameter = 40
        write("POP!")


draw_balloon()

onkey(inflate_balloon, "Up")
listen()

turtle.done()  # will keep the GUI open until user closes
