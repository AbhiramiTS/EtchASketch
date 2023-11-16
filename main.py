import turtle

# Create a turtle named 'timmy' and set its shape to "turtle"
timmy = turtle.Turtle()
timmy.shape("turtle")

# Create a turtle screen
screen = turtle.Screen()

# Function to move the turtle forward
def move_forward():
    timmy.forward(10)

# Function to move the turtle up
def move_up():
    timmy.left(10)
    timmy.forward(10)

# Function to move the turtle backward
def move_backward():
    timmy.backward(10)

# Function to move the turtle down
def move_down():
    timmy.right(10)
    timmy.forward(10)

# Function to clear the screen and reset the turtle's position
def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# Set up key listeners for different keys
screen.listen()
screen.onkey(key="a", fun=move_forward)
screen.onkey(key="q", fun=move_up)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="z", fun=move_down)
screen.onkey(key="c", fun=clear_screen)

# Close the turtle screen when clicked
screen.exitonclick()
