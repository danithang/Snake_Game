from turtle import Turtle

# constants which will be global variable is in all caps
# x positions are going to be in different places along the x-axis while y remains at 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# creating move distance to pass it in self.all_snakes.forward in move_snake function
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# creating Snake class
class Snake:
    def __init__(self):
        # having all_snakes in empty list to append to it later
        self.all_snakes = []
        self.create_snake()
        # creating head of snake and saying its equal to all_snakes original position
        self.head = self.all_snakes[0]

    def create_snake(self):
        # for loop to take each 20x20 snake(square) and give them color, place them at right positions and append
        # them in all_snakes list...all of that is in add_snake then calling that function and outputting position
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snakes.append(new_snake)

    # extending snake...[-1] means counting from end of list...for example [1, 2, 3] 3 would be considered in
    # position -1...getting hold of position() which is a turtle class, adding new segment(add_segment) to same
    # position as last position
    def extend(self):
        self.add_snake(self.all_snakes[-1].position())

    def move_snake(self):
        # for loop to get the snake number at a range from start, stop, and step, taking from range(0, 3) in first for
        # loop, start=position 2, stop=position 0 and step=-1 because we are counting down instead of up getting the
        # length of all_snakes which is 2 acts the same as putting 2 in start position, the -1 is subtracting the fact
        # that we count to 3 without counting 3
        for snake_num in range(len(self.all_snakes) - 1, 0, -1):
            # having each snake go to the second to last position on x and y coordinate axis
            new_x = self.all_snakes[snake_num - 1].xcor()
            new_y = self.all_snakes[snake_num - 1].ycor()
            # telling snake to go from the last position to second to last position and continue
            self.all_snakes[snake_num].goto(new_x, new_y)
        # outside the for loop to get snake to continue moving by calling the original all_snakes at the 0 position
        # from the beginning x and y coordinates to move forward
        self.head.forward(MOVE_DISTANCE)

    # defining up, down, right, left by setting the heading whatever degrees it needs to go, up=90, down=270, right=0,
    # left=180
    def up(self):
        # saying if current heading is pointing down then it can't move up, if moving up, right, or left it can move up,
        # basically saying the head of the snake can't move backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
