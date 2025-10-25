import turtle
import random
score =0
sea=turtle.Screen()
sea.bgpic("sea.gif")
sea.addshape("girl1.gif")
sea.addshape("girl2.gif")
sea.addshape("coin.gif")
hunter = turtle.Turtle()
hunter.shape("girl1.gif")
hunter.penup()
hunter.goto(0,-150)
scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.speed(500)
scoreboard.goto(-100,240)
scoreboard.write("Score : 0",font=("Courier",33,"bold"))
scoreboard.hideturtle()
coin = turtle.Turtle()
coin.speed(1000)
coin.shape("coin.gif")
coin.penup()
coin.goto(-280,280)
def right():
    hunter.shape("girl1.gif")
    hunter.fd(5)
def left():
    hunter.shape("girl2.gif")
    hunter.bk(5)
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()  
def move():
    y=coin.ycor()
    coin.sety(y-3)
while True:
    sea.update()
    move()
    if coin.ycor() < -300:
        x = random.randint(-280,280)
        coin.goto(x,280)
    if hunter.distance(coin) < 50:
        score = score+1
        scoreboard.clear()
        scoreboard.write("Score :{}".format(score),font=("Courier",33,"bold"))#TO update the score I used the curly brackets
        
        x = random.randint(-280,280)
        coin.goto(x,280)
turtle.done()