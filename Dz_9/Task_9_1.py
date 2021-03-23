from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "red", "yellow", "green"

    def running(self):
        while True:
            for c in self.__color:
                print(c)
                if c[0]:
                    sleep(7)
                elif c[1]:
                    sleep(2)
                elif c[2]:
                    sleep(7)


obj = TrafficLight()
obj.running()

# _______________________________альтернативное решение с черепахой__________________________________________________
from turtle import *
from time import sleep

t = Turtle()
t.screen.setup(600, 600)


def circle(x, y, r):
    t.up()
    t.goto(x, y - r)
    t.down()
    t.color("grey")
    t.circle(r, 360)


def circle_filled(x, y, r, color):
    t.up()
    t.goto(x, y - r)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r, 360)
    t.end_fill()


def rectangle(x, y, width, height):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.end_fill()
    t.right(90)


class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def running(self):
        rectangle(16, 190, 70, 180)
        circle(50, 150, 25)
        circle(50, 100, 25)
        circle(50, 50, 25)
        while True:
            circle_filled(50, 150, 25, self.__color[0])
            sleep(7)
            t.undo()
            circle_filled(50, 100, 25, self.__color[1])
            sleep(2)
            t.undo()
            circle_filled(50, 50, 25, self.__color[2])
            sleep(5)
            t.undo()


obj = TrafficLight()
obj.running()

t.screen.exitonclick()
t.screen.mainloop()