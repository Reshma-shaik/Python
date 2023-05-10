"""
    TODO: Add description for this file
"""
from turtle import Turtle, Screen

# Initialize turtle object to perform actions.
turtle = Turtle()
# Initialize the screen object to control the screen.
screen = Screen()

# Create Spirograph using Turtle
turtle.speed("fastest")

for _ in range(int(360/10)):
    turtle.circle(100)
    turtle.setheading(turtle.heading()+10)
