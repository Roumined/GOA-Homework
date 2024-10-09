from turtle import *

#we want to paint a house

#step 1: draw a square

shape("turtle")
speed(3)
width(7)
color("purple")

begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#end of square

#drawing a door

forward(70)
color("yellow")
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)

penup()
goto(130, 60)
pendown()

right(90)
forward(20)

#end of door

#drawing a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(60)

forward(200)
left(120)

forward(200)
end_fill()

#end of roof

#drawing a windows

color("yellow")
penup()
goto(10, 125)
pendown()

right(150)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

penup()
goto(10, 145)
pendown()

right(180)
forward(40)

penup()
goto(30, 125)
pendown()

left(90)
forward(40)

penup()
goto(190, 125)
pendown()

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)

penup()
goto(170, 125)
pendown()

left(90)
forward(40)

penup()
goto(150, 145)
pendown()

right(90)
forward(40)

penup()
goto(80, 250)
pendown()

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

penup()
goto(80, 270)
pendown()

forward(40)

penup()
goto(100, 250)
pendown()

left(90)
forward(40)

#end of windows

exitonclick()