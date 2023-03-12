import colorgram
from turtle import Turtle, Screen
from random import choice

colors = colorgram.extract('image.jpg',30)
mycolor = []
for _ in colors:
    # print(_.rgb)
    # print(_.rgb[0])
    # print(_.rgb[1])
    # print(_.rgb[2])
    mycolor.append((_.rgb.r,_.rgb.g,_.rgb.b))


#print(mycolor)

myturtle = Turtle()
myscreen = Screen()
myscreen.colormode(255)

myturtle.hideturtle()
myturtle.penup()
myturtle.goto(-325,-325)


for i in range(0,10):
    for j in range(0,10):
        myturtle.dot(20, choice(mycolor))
        myturtle.setx(myturtle.position()[0]+50)
    myturtle.goto(-325, myturtle.position()[1] + 50)

myscreen.exitonclick()