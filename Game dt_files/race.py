import turtle
road = turtle.Screen()
road.addshape("redcar.gif")
road.addshape("bluecar.gif")
road.bgpic("race.gif")
redcar=turtle.Turtle()
redcar.setheading(90)
redcar.shape("redcar.gif")
redcar.penup()
redcar.goto(-100,-240)
bluecar=turtle.Turtle()
bluecar.setheading(90)
bluecar.shape("bluecar.gif")
bluecar.penup()
bluecar.goto(100,-240)
def player1():
    redcar.fd(5)
def player2():
    bluecar.fd(5)
turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")
#pos - To find the position of the pointer
turtle.listen()
while True:
    road.update()
    if redcar.pos() > (-100,200):
        road.bgpic("redcarwins.gif")
    if bluecar.pos() > (100,200):
        road.bgpic("bluecarwins.gif")
turtle.done()