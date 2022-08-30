from turtle import Turtle
import random


# class inheritance, Food will do everything already established in Turtle and add to it
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # changing the shape of the length and width of circle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    # defining a refresh method to put the circle(food) in a different random location when snake collides with food
    def refresh(self):
        # adding random so the circle(food) goes to a random location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


