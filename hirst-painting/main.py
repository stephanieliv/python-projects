import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.shape("circle")
tim.speed("slow")
t.colormode(255)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), 
              (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), 
              (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), 
              (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), 
              (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
x = -220
y = -200


def set_position(X, Y):
    tim.penup()
    tim.ht()
    tim.setx(X)
    tim.sety(Y)


def draw_dots():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.ht()
        tim.forward(50)
    tim.home()


for _ in range(10):
    set_position(x, y)
    draw_dots()
    y += 50


screen.exitonclick()
