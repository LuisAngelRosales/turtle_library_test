from turtle import  Turtle, Screen
from random import Random

import colorgram


random=Random()
timmy = Turtle()
screen=Screen()
height_traveled=0
width_traveled=0
x=-screen.window_width()/2.1
y=-screen.window_height()/2.1

colors=colorgram.extract('1200x878.jpg',30)
color_list=[]
for color in colors:
    color_list.append(color.rgb)
def generate_random_number():
    return randint(1,255)
screen.colormode(255)
screen.bgcolor(221,214,201)
def create_painting():
    global y
    global  width_traveled
    global height_traveled
    timmy.up()
    timmy.goto(-screen.window_width()/2.1, -screen.window_height()/2.1)
    timmy.pensize(10)

    timmy.speed(0)
    while True:
        rgb=random.choice(color_list)
        timmy.pencolor(rgb)
        timmy.dot(25)
        timmy.fd(50)
        width_traveled+=50
        if width_traveled>=screen.window_width():
            y+=50
            height_traveled+=50
            timmy.setpos(x,y)
            width_traveled=0
        if height_traveled >= screen.window_height():
            screen.exitonclick()
            break


print(screen.screensize())
create_painting()
