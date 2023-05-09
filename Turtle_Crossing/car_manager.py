from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager():
    def __init__(self):
        self.cars = [] # init, needs to add self. here this is only a list, no need to inherit turtle

    def make_car(self):
        random_chance = random.randint(1,9)
        if random_chance == 1: # to make sure the new car is generated nearly every 9th time of the loop
            new_y = random.randint(-250, 251)
            new_car = Turtle() # new car should be a turtle object
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(300, new_y)
            self.cars.append(new_car) # everytime create a new car, need to append it in the list

    def move(self, level):
        for car in self.cars: # need to call the init, so use self
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level - 1))
