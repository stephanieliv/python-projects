from turtle import Turtle, Screen

bert = Turtle()
screen = Screen()
screen.listen()


def forwards():
    bert.forward(10)


def backwards():
    bert.backward(10)


def counter_clockwise():
    bert.left(15)


def clockwise():
    bert.right(15)


def clear_drawing():
    bert.clear()
    bert.penup()
    bert.home()


screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
