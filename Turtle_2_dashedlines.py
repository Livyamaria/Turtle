import turtle as t
from turtle import Screen

timmy_the_turtle = t.Turtle()
Screen().bgcolor("yellow")
t.color("red")
t.shape("turtle")
t.speed('normal')
t.pencolor(("red"))
for i in range(10):

   t.forward(90)
   t.penup()
   t.forward(90)
   
   t.pendown()
   t.left(90)

