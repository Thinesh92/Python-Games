import turtle
b = turtle.Turtle()
b.goto(-230,230)
b.fillcolor("black")
b.begin_fill()
for i in range(4):
    b.fd(450)
    b.rt(90)
b.end_fill()
b.speed(3)  # Set the speed of the turtle
b.color("yellow")
b.fillcolor("yellow")

batman_points = [
    (0,-3), (1,-1), (2,-2), (3,-1), (4,-2), (7,0), (3,3), (1,1), (1,1.5), (1,3),
    (0.5,2), (0,2), (-0.5,2), (-1,3), (-1,1.5), (-1,1), (-3,3), (-7,0), (-4,-2),
    (-3,-1), (-2,-2), (-1,-1), (0,-3) 
]
scale = 30  

# Move turtle to starting position
b.penup()
b.goto(batman_points[0][0] * scale, batman_points[0][1] * scale)
b.pendown()
b.begin_fill()

# Draw the Batman logo
for point in batman_points:
    b.goto(point[0] * scale, point[1] * scale)

b.end_fill()

# Hide the turtle
b.hideturtle()

# Display the window
turtle.done()
