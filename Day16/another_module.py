from turtle import Turtle, Screen


my_turtle = Turtle()
my_turtle.shape("turtle")  # Set the shape to a turtle
my_turtle.color("purple")
my_turtle.forward(100)  # Move forward 100 pixels
my_turtle.right(70)  # Turn right 90 degrees
my_turtle.forward(100)  # Move forward 100 pixels

my_screen = Screen()
my_screen.canvheight = 500
my_screen.canvwidth = 500
my_screen.bgcolor("white")
my_screen.exitonclick()
