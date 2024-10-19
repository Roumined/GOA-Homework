from turtle import *

#we want to draw a mansion

#we want to draw the structure 

shape("circle")
width(2)
speed(13)

forward(400)
left(90)

forward(250)
left(70)

forward(425)
left(110)

forward(395)

penup()
goto(420, 240)
pendown()

right(115)
forward(25)

penup()
goto(-20, 405)
pendown()

right(180)
forward(25)

penup()
goto(420, 240)
pendown()

left(115)
forward(25)

left(70)
forward(460)

left(90)
forward(20)

penup()
goto(380, 280)
pendown()

right(160)
forward(220)

left(100)
forward(220)

left(80)
forward(105)

penup()
goto(400, 505)
pendown()

right(75)
forward(25)

penup()
goto(163, 462)
pendown()

right(3)
forward(25)

right(100)
forward(20)

right(82)
forward(265)

right(100)
forward(18)

#end of structure

#we want to draw a door

penup()
goto(190, 0)
pendown()

right(180)
forward(130)

right(90)
forward(70)

right(90)
forward(130)

penup()
goto(190, 65)
pendown()

left(90)
width(3)
forward(15)

width(2)

penup()
goto(170, 0)
pendown()

left(90)
forward(160)

right(90)
forward(110)

right(90)
forward(160)

penup()
goto(150, 0)
pendown()

right(180)
forward(180)

right(90)
forward(150)

right(90)
forward(180)
width(2)

#end of door

#we want to draw a windows

penup()
goto(190, 380)
pendown()

left(90)
forward(160)

left(90)
forward(50)

left(90)
forward(160)

left(90)
forward(50)

penup()
goto(20, 30)
pendown()

right(180)
forward(140)

right(90)
forward(40)

right(90)
forward(140)

right(90)
forward(40)

penup()
goto(80, 30)
pendown()

right(90)
forward(140)

right(90)
forward(40)

right(90)
forward(140)

right(90)
forward(40)

penup()
goto(20, 200)
pendown()

left(180)
forward(150)

left(90)
forward(50)

left(90)
forward(150)

left(90)
forward(50)

penup()
goto(20, 280)
pendown()

left(90)
forward(150)

left(90)
forward(40)

left(70)
forward(160)

left(110)
forward(95)

penup()
goto(380, 30)
pendown()

right(180)
forward(140)

left(90)
forward(60)

left(90)
forward(140)

left(90)
forward(60)

#end of windows

#here I added a small detail in the center of the house

penup()
goto(190, 210)
pendown()

forward(180)
left(90)

forward(10)
left(90)

forward(180)
left(90)

forward(10)

#end of this part

#we want to draw window frames

penup()
goto(17, 27)
pendown()

left(90)
forward(46)

left(90)
forward(146)

left(90)
forward(46)

left(90)
forward(146)

penup()
goto(77, 27)
pendown()

left(90)
forward(46)

left(90)
forward(146)

left(90)
forward(46)

left(90)
forward(146)

penup()
goto(383, 27)
pendown()

right(90)
forward(66)

right(90)
forward(146)

right(90)
forward(66)

right(90)
forward(146)

penup()
goto(187, 377)
pendown()

left(90)
forward(166)

left(90)
forward(56)

left(90)
forward(166)

left(90)
forward(56)

penup()
goto(17, 197)
pendown()

left(90)
forward(156)

left(90)
forward(56)

left(90)
forward(156)

left(90)
forward(56)

penup()
goto(17, 277)
pendown()

left(90)
forward(156)

left(90)
forward(46)

left(70)
forward(166)

left(110)
forward(102)

penup()
goto(187, 0)
pendown()

right(180)
forward(133)

right(90)
forward(76)

right(90)
forward(133)

#end of window frames

#we want to add some color

penup()
goto(170, 0)
pendown()

color("black")
begin_fill()
left(180)
forward(160)

right(90)
forward(110)

right(90)
forward(160)

left(90)
forward(20)

left(90)
forward(180)

left(90)
forward(150)

left(90)
forward(180)

left(90)
forward(20)
end_fill()

penup()
goto(80, 30)
pendown()

color("black")
begin_fill()
left(75)
forward(145)

right(164)
forward(138)

right(90)
forward(40)
end_fill()

penup()
goto(20, 30)
pendown()

color("black")
begin_fill()
right(106)
forward(145)

right(164)
forward(138)

right(90)
forward(40)
end_fill()

penup()
goto(320, 30)
pendown()

color("black")
begin_fill()
right(114)
forward(150)

right(157)
forward(138)

right(90)
forward(40)
end_fill()

penup()
goto(190, 380)
pendown()

color("black")
begin_fill()
right(162)
forward(166)

right(108)
forward(50)

right(90)
forward(157)
end_fill()

penup()
goto(20, 200)
pendown()

color("black")
begin_fill()
right(161)
forward(158)

right(108)
forward(50)

right(91)
forward(150)
end_fill()

penup()
goto(20, 280)
pendown()

color("black")
begin_fill()
right(150)
forward(117)

right(52)
forward(50)

right(66)
forward(40)

right(92)
forward(150)
end_fill()

penup()
goto(190, 210)
pendown()

color("black")
begin_fill()
left(90)
forward(5)

left(91)
forward(179)

left(89)
forward(2)

left(90)
forward(180)
end_fill()

penup()
goto(270, 255)
pendown()

#end of this part

exitonclick()