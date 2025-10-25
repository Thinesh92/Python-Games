import turtle
import random

segment = []

# Background Image
grass = turtle.Screen()
grass.bgpic("grass.gif")
grass.setup(600, 600)
grass.addshape("headup.gif")
grass.addshape("headdown.gif")
grass.addshape("headleft.gif")
grass.addshape("headright.gif")
grass.addshape("body.gif")

# Snake
snake = turtle.Turtle()
snake.penup()
snake.speed(5)
snake.goto(0, 0)
snake.setheading(90)
snake.shape("headup.gif")

# Food
food = turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.speed(500)
food.goto(100, 10)

# Score
pen = turtle.Turtle()
pen.penup()
pen.speed(500)
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: ", font=("Courier", 27, "bold"))

# Movement
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
game_over=False
score = 0
while not game_over:
    grass.update()

    if snake.xcor() > 290 or snake.xcor() <-290 or snake.ycor()>290 or snake.ycor()<-290:
        grass.bgpic("gameover.gif")
        food.hideturtle()
    for i in segment:
        if i.distance(snake)<20:
            grass.bgpic("gameover.gif")
            food.hideturtle
    if snake.distance(food) < 10:
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        food.setpos(x, y)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), font=("Courier", 27, "bold"))
        body = turtle.Turtle()
        body.penup()
        body.shape("body.gif")
        body.speed(0)
        segment.append(body)

    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)
    move()
turtle.done()
