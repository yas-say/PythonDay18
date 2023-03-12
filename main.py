from turtle import Turtle, Screen
from random import randint, choice

def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0,255)
    tup = (r, g, b)
    return tup

def draw_Square(turtle):
    for _ in range(4):
        draw_Dash(turtle)
        turtle.right(90)



def draw_Dash(turtle):
    for _ in range(50):
        if _ % 2 == 1:
            turtle.pendown()
            turtle.forward(10)
        else:
            turtle.penup()
            turtle.forward(10)

def draw_shapes(turtle):
    turtle.pensize(5)
    for _ in range(3,11):
        turtle.home()
        turtle.color(random_color())
        angle = 360/_
        for i in range(0, _):
            print(f"i={i}")
            turtle.forward(100)
            turtle.right(angle)


def draw_RandomWalk(turtle):
    direction=[0,90,180,270]
    turtle.pensize(15)
    turtle.speed(0)
    turtle.hideturtle()
    for _ in range(200):
        turtle.pencolor(random_color())
        turtle.setheading(choice(direction))
        turtle.forward(25)


def draw_spiro(turtle):
    turtle.speed(0)
    turtle.pensize(2)
    for angle in range (0,360,2):
        turtle.setheading(angle)
        turtle.pencolor(random_color())
        turtle.circle(100)




my_turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)
#my_turtle.shape("circle")

#draw_Square(my_turtle)
#draw_Dash(my_turtle)
#draw_shapes(my_turtle)
#draw_RandomWalk(my_turtle)
#draw_spiro(my_turtle)


my_screen.exitonclick()
