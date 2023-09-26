from turtle import *
from math import *


#we want to piant a house
speed(1)
width(8)


color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)


forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90) 
forward(120)


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(15,130)
pendown()


left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)


penup()
goto(145,150)
pendown()


forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)


exitonclick()
