from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (0, 0), (-20, 0)]  # in Python, all constants are all caps
MOVE_DISTANCE = 20
# set heading angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_squares(position)

    def add_squares(self, position):
        new_square = Turtle()
        new_square.shape("square")
        new_square.color("white")
        new_square.penup()  # remove the moving lines
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_squares(self.squares[-1].position())

    def move(self):
        for sq_num in range(len(self.squares) - 1, 0,-1):  # all the squares move to its previous square's positions, except the first square
            new_x = self.squares[sq_num - 1].xcor()
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
