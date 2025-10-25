import turtle
import random
p=turtle.Turtle()
def rectangle():
 x=random.randint(-300,300)
 y=random.randint(-300,300)
 p.goto(x,y)
 p.pendown()
 p.fillcolor("red")
 p.begin_fill()
 for i in range(2):
    p.fd(100)
    p.lt(90)
    p.fd(50)
    p.lt(90)
 p.end_fill()
 p.penup()

# rectangle()
# p.goto(100,100)
# rectangle()
# p.goto(-100,100)
# rectangle()
turtle.onkey(rectangle,"Up")
turtle.listen()
turtle.done()