import turtle
p = turtle.Turtle()

p.goto(-200,200)
p.fillcolor("black")
p.begin_fill()

for i in range(4):
    p.fd(400)
    p.rt(90)
p.end_fill()

p.goto(-80,140)
p.color("red")
p.fillcolor("red")
p.begin_fill()
p.goto(-80,-140)
p.goto(-20,-140)
p.goto(-20,140)
p.goto(-80,140)
p.end_fill()
p.penup()
p.goto(80,140)
p.pendown()

p.begin_fill()
p.goto(80,-140)
p.goto(20,-140)
p.goto(20,140)
p.goto(80,140)
p.end_fill()

p.penup()
p.goto(-80,140)
p.pendown()

p.begin_fill()
p.goto(-20,140)
p.goto(80,-140)
p.goto(20,-140)
p.goto(-80,140)
p.end_fill()

turtle.done()