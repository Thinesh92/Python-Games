import turtle
p=turtle.Turtle()
# for i in range(360):
#  p.fd(1)
#  p.lt(1)
# turtle.done()
s= turtle.Screen()
p.width(10)
p.penup()
p.goto(-125,45)
p.pendown()
p.fillcolor("yellow")
p.begin_fill()

p.goto(125,45)
p.lt(90)
p.fd(65)
for i in range(180):
    p.fd(2.1)
    p.lt(1)
p.fd(65)
p.end_fill()

p.fd(125)
for i in range(180):
    p.fd(2.1)
    p.lt(1)
p.fd(125)

#Eyes and mouth
p.width(30)
p.penup()

p.goto(60,20)
p.pendown()
p.goto(60,-30)
p.penup()

p.goto(-60,20)
p.pendown()
p.goto(-60,-30)

p.penup()

p.goto(-75,-75)
p.pendown()

p.width(10)
p.lt(180)

for i in range(180):
    p.fd(1.4)
    p.lt(1)
    
turtle.done()