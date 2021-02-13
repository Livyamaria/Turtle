import turtle as t
from turtle import Screen

timmy_the_turtle = t.Turtle()
Screen().bgcolor("yellow")
t.color("red")

for _ in range(4):

    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)