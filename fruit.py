from turtle import Turtle
from random import randint

class Fruit:
    POSITION = (randint(0, 580), randint(0, 580))

    def __init__(self):
        self.create_fruit()

    def create_fruit(self):
        fruit = Turtle("square")
        fruit.goto(10, 10)
        fruit.up()
        fruit.color("red")
        fruit.goto(self.POSITION)