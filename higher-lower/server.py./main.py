from flask import Flask
import random

random_number = random.randint(0, 10)
print(random_number)

app = Flask(__name__)


@app.route("/")
def start():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:number>")
def guess(number):
    if number > random_number:
        return f"Sorry {number} is too high!" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif number < random_number:
        return f"Sorry {number} is too low!" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    else:
        return "Correct!" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
