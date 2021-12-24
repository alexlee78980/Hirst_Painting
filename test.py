import turtle
from turtle import Turtle, Screen
import colorgram
import random

turtle.colormode(255)
dot = Turtle()

screen = Screen()
# colors = colorgram.extract("p.jpg", 50)
color_list = [(211, 154, 98), (53, 107, 131),
              (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130),
              (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143),
              (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22),
              (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72),
              (183, 190, 204), (78, 66, 42), (23, 99, 96)]
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     t = (r,g,b)
#     color_list.append(t)
# print(color_list)
dot.penup()
start_y = -250
start_x = -250
dot.setposition(start_x, start_y)
for i in range(0, 10):
    for l in range(0, 10):
        choice = random.choice(color_list)
        dot.dot(30, choice)
        dot.forward(50)
    start_y += 50
    dot.setposition(start_x, start_y)
screen.exitonclick()
