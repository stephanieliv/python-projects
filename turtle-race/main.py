from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x = -230
y = -100


#def race_start(X, Y):
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    all_turtles.append(new_turtle)


while user_bet:
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle was the winner!")
            else:
                print(f"You lose! The {winning_turtle} turtle was the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


#race_start(x, y)


screen.exitonclick()
