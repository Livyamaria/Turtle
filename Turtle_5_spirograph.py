import turtle as t
import random
from turtle import Screen
t.colormode(255)
tim = t.Turtle()
tim.pensize(10)
Screen().bgcolor("black")
tim.speed("fastest")
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour=(r,g,b)
    return random_colour


for i in range(1000):
 tim.color(random_color())
 tim.circle(random.randint(0,50))
 tim.left(90)