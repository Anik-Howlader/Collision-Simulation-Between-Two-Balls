import time
import turtle as t
import random
import math

screen = t.Screen()
screen.setup(width=800, height=650)
screen.bgcolor("Black")
header = t.Turtle()
header.penup()
header.goto(0,270)
header.pendown()
header.color("white")
header.write("Collision Simulation Between Two Balls", font=("Verdana",15, "normal"),align="center")
header.hideturtle()


x = -250
y = -250
angle = 90
r1 = 40
r2 = 20
m1 = r1/10
m2 = r2/10
boundary = t.Turtle()
boundary.shape('square')
boundary.penup()
boundary.goto(x, y)
boundary.pendown()
boundary.color("cyan")
boundary.pensize(2)
for i in range(4):
    boundary.forward(abs(2*x))
    boundary.left(angle)
boundary.hideturtle()


coll = t.Turtle()
coll.penup()
coll.goto(0,-280)
coll.pendown()
coll.color("white")
coll.write("No Collision", font=("Verdana",12, "normal"),align="center")
coll.hideturtle()

ball1 = t.Turtle()
ball2 = t.Turtle()
ball1.shape("circle")
ball2.shape("circle")
ball1.color("#FF204E")
ball2.color("#836FFF")
ball1.penup()
ball1.shapesize(r1 / 10)
ball1.velocity = (2, 2)
ball2.penup()
ball2.shapesize(r2 / 10)
ball2.velocity = (5, 5)
ball1.goto(-80, 0)
ball2.goto(50, 0)

total = 0



while True:

    x1, y1 = ball1.position()
    x2, y2 = ball2.position()
    distance = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
    if distance < (r1 + r2):
        coll.clear()
        total = total+1
        seconds = time.time()
        curr = time.ctime(seconds)
        s = "["+str((x2-x1)/2)+","+ str((y2 - y1) / 2)+"]"+" Last Time :"+str(curr)+" Total :"+str(total)
        coll.write("Collision location : "+s, font=("Verdana", 10, "normal"), align="center")
        print("x : ", (x2-x1)/2 , "\n")
        print("y : " , (y2 - y1) / 2 , "\n")
        v1x, v1y = ball1.velocity
        v2x, v2y = ball2.velocity

        new_v1x = ((m1 - m2) * v1x + 2 * m2 * v2x) / (m1 + m2)
        new_v1y = ((m1 - m2) * v1y + 2 * m2 * v2y) / (m1 + m2)
        new_v2x = ((m2 - m1) * v2x + 2 * m1 * v1x) / (m1 + m2)
        new_v2y = ((m2 - m1) * v2y + 2 * m1 * v1y) / (m1 + m2)

        ball1.velocity = (new_v1x, new_v1y)
        ball2.velocity = (new_v2x, new_v2y)

    elif ball1.xcor() > -x - r1 or ball1.xcor() < x + r1:
        ball1.velocity = (-ball1.velocity[0], ball1.velocity[1])
    elif ball1.ycor() > -x - r1 or ball1.ycor() < x + r1:
        ball1.velocity = (ball1.velocity[0], -ball1.velocity[1])
    elif ball2.xcor() > -y - r2 or ball2.xcor() < y + r2:
        ball2.velocity = (-ball2.velocity[0], ball2.velocity[1])
    elif ball2.ycor() > -y - r2 or ball2.ycor() < y + r2:
        ball2.velocity = (ball2.velocity[0], -ball2.velocity[1])
    a1 = ball1.xcor() + ball1.velocity[0]
    b1 = ball1.ycor() + ball1.velocity[1]
    a2 = ball2.xcor() + ball2.velocity[0]
    b2 = ball2.ycor() + ball2.velocity[1]

    if a1 < x:
        a1=x+r1
    if b1 < y:
        b1=x+r1
    if a1 > -x:
        a1=-x-r1
    if b1 > -y:
        b1=-y-r1
    if a2 < x:
        a2=x+r2
    if b2 < y:
        b2=y+r2
    if a2 > -x:
        a2=-x-r2
    if b2 > -y:
        b2=-y-r2

    ball1.goto(a1,b1)
    ball2.goto(a2, b2)
    screen.update()

