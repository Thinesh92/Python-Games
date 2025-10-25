import turtle

# Create the screen
space = turtle.Screen()
space.tracer(0)  # Turn off automatic updates for smoother animation

# Set background
#space.bgpic("space1.gif")
space.bgpic("space1.gif")


# Add shapes
space.addshape("astro1.gif")
space.addshape("rocketup.gif")
space.addshape("rocketdown.gif")
space.addshape("rocketleft.gif")
space.addshape("rocketright.gif")

# Create astronaut
spaceman = turtle.Turtle()
spaceman.shape("astro1.gif")
spaceman.penup()
spaceman.goto(-103, 255)

# Create rocket
rocket = turtle.Turtle()
rocket.shape("rocketup.gif")
rocket.penup()
rocket.goto(180, -250)
rocket.speed(0)  # Max speed

# Define movement functions
def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.shape("rocketup.gif")
    space.update()

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.shape("rocketdown.gif")
    space.update()

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.shape("rocketleft.gif")
    space.update()

def right():
    rocket.setheading(0)
    rocket.forward(10)
    rocket.shape("rocketright.gif")
    space.update()

# Listen for keypresses
turtle.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

# Main game loop
while True:
    space.update()
    
    # Check for collision with astronaut
    if rocket.distance(spaceman) < 10:
        space.bgpic("final1.gif")
        break  # Stop the loop when the rocket reaches the astronaut

turtle.done()
