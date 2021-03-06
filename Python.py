import turtle

t = turtle.Turtle()

# draw speed
t.speed("normal")

t.penup()
t.pensize(5)
t.pencolor("black")

# head-top
t.goto(0, 315)
t.setheading(80)
t.fillcolor("yellow")
t.pendown()
t.begin_fill()
t.circle(-40, 200)
t.penup()
t.end_fill()
t.goto(10, 315)
t.setheading(80)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.circle(-30, 200)
t.penup()
t.end_fill()

# face-outside
t.goto(-150, 280)
t.pendown()
t.setheading(200)
t.circle(180, 160)
t.setheading(-7)
t.circle(500, 15)
t.circle(180, 110)
t.setheading(151)
t.circle(700, 28)
t.setheading(27)
t.circle(-200, 32)
t.setheading(23)
t.circle(-120, 80)
t.setheading(-28)
t.circle(-200, 32)
t.penup()

# head-style
t.goto(-150, 280)
t.setheading(20)
t.pendown()
t.circle(-200, 45)
t.setheading(3)
t.circle(-150, 45)
t.setheading(-9)
t.circle(-100, 30)
t.penup()

# face-style
t.goto(-80, 278)
t.pencolor("orange")
t.setheading(-158)
t.pendown()
t.circle(200, 119)
t.penup()
t.goto(-30, 270)
t.setheading(-135)
t.pendown()
t.circle(300, 70)
t.penup()
t.goto(40, 253)
t.setheading(-78)
t.pendown()
t.circle(-500, 38)
t.penup()
t.goto(120, 222)
t.setheading(-55)
t.pendown()
t.circle(-200, 90)
t.penup()

# eyes-outside
t.goto(-195, 185)
t.setheading(50)
t.pencolor("black")
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.circle(-80, 90)
t.setheading(7)
t.circle(-40, 90)
t.setheading(-60)
t.circle(40, 90)
t.setheading(40)
t.circle(-60, 30)
t.setheading(1)
t.circle(-50, 110)
t.setheading(-30)
t.circle(-25, 200)
t.setheading(210)
t.circle(-200, 73)
t.setheading(200)
t.circle(-40, 150)
t.setheading(117)
t.circle(-30, 115)
t.penup()
t.end_fill()

# r-hand
t.goto(-150, -60)
t.setheading(-35)
t.pendown()
t.circle(200, 70)
t.setheading(-40)
t.circle(-200, 15)
t.setheading(-60)
t.circle(-40, 130)
t.penup()

# body
t.goto(40, -80)
t.setheading(-50)
t.pendown()
t.circle(-150, 50)
t.setheading(-85)
t.circle(-70, 60)
t.setheading(-120)
t.circle(-40, 120)
t.setheading(-150)
t.circle(-60, 70)
t.setheading(130)
t.circle(-100, 20)
t.setheading(130)
t.circle(-150, 65)
t.penup()

# l-hand
t.goto(-145, -120)
t.setheading(170)
t.pendown()
t.circle(-200, 20)
t.setheading(140)
t.circle(-40, 115)
t.penup()

# body-style
t.goto(-143, -150)
t.pendown()
t.goto(-123, -150)
t.goto(-110, -80)
t.penup()

# feet-style
t.goto(-107, -230)
turtle.colormode(255)
t.pencolor(255, 228, 181)
t.setheading(23)
t.pendown()
t.circle(-20, 70)
t.setheading(27)
t.circle(-20, 90)
t.setheading(20)
t.circle(-20, 90)
t.setheading(45)
t.circle(-20, 90)
t.setheading(37)
t.circle(-20, 90)
t.setheading(35)
t.circle(-20, 80)
t.penup()

# logo
t.goto(-100, -180)
t.pendown()
t.pencolor("blue")
t.circle(20)
t.penup()
t.goto(-75, -203)
t.pendown()
t.pencolor("yellow")
t.circle(20)
t.penup()
t.goto(-50, -186)
t.pendown()
t.pencolor("black")
t.circle(20)
t.penup()
t.goto(-25, -209)
t.pendown()
t.pencolor("green")
t.circle(20)
t.penup()
t.goto(0, -192)
t.pendown()
t.pencolor("red")
t.circle(20)
t.penup()

# l-eye
t.goto(-140, 130)
t.pencolor("black")
t.fillcolor("black")
t.setheading(5)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.goto(-143, 145)
t.pencolor("white")
t.fillcolor("white")
t.setheading(1)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

# r-eye
t.goto(12, 90)
t.pencolor("black")
t.fillcolor("black")
t.setheading(5)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.goto(7, 105)
t.pencolor("white")
t.fillcolor("white")
t.setheading(1)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

# face-inside-style
t.goto(-190, 95)
t.pencolor("pink")
t.fillcolor("pink")
t.setheading(5)
t.begin_fill()
t.pendown()
t.circle(12)
t.penup()
t.end_fill()
t.goto(35, 50)
t.setheading(5)
t.begin_fill()
t.pendown()
t.circle(12)
t.penup()
t.end_fill()

t.hideturtle()
turtle.done()
