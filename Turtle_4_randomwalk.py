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

directions = [0, 90, 180, 270]
for _ in range(200):
 colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
 tim.color(random_color())
 tim.forward(30)
 tim.setheading(random.choice(directions))
