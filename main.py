from turtle import Turtle, Screen, resetscreen
from random import randint

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.fd(10)


def move_backward():
    timmy.backward(10)


def move_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear_screen():
    resetscreen()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(clear_screen, "c")

screen.exitonclick()
