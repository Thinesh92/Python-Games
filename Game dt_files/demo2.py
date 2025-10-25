import turtle
import random

grass = turtle.Screen()
grass.bgpic("grass.gif")
grass.addshape("headup.gif")
grass.addshape("headdown.gif")
grass.addshape("headright.gif")
grass.addshape("headleft.gif")
grass.addshape("body.gif")
grass.addshape("gameover.gif")


snake = turtle.Turtle()
snake.penup()
snake.speed(5)
snake.goto(0, 0)
snake.setheading(90)
snake.shape("headup.gif")

food = turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.speed(500)
food.goto(100, 10)


pen = turtle.Turtle()
pen.penup()
pen.speed(500)
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: ", font=("Courier", 27, "bold"))


def move():
    snake.fd(5)


def up():
    if snake.heading() != 270:
        snake.setheading(90)
        snake.shape("headup.gif")

def down():
    if snake.heading() != 90:
        snake.setheading(270)
        snake.shape("headdown.gif")

def right():
    if snake.heading() != 180:
        snake.setheading(0)
        snake.shape("headright.gif")

def left():
    if snake.heading() != 0:
        snake.setheading(180)
        snake.shape("headleft.gif")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.listen()

while True:
    
    move()




turtle.done()


