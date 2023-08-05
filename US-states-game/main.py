import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Ariel", 10, "normal")

score = 0
screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="Name another US state:").title()
    if answer_state == "Exit":
        states_to_learn = [new_state for state in states if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States to learn.csv")
        break

    for state in states:
        if answer_state == state:
            guessed_states.append(state)
            state_data = data[data.state == state]
            x = int(state_data.x)
            y = int(state_data.y)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(x, y)
            state.write(f"{answer_state}", False, ALIGNMENT, FONT)
            score += 1



screen.exitonclick()
