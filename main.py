from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn off animation tracing on screen
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# getting the screen to listen to manual keyboard clicks, binding them to the direction pad on keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# while loop to move the snake in all directions
is_game_on = True
while is_game_on:
    # get the screen to refresh after all snakes have moved forward as one
    screen.update()
    # delay refresh after each snake moves
    time.sleep(0.1)
    snake.move_snake()
    # Detect collision with food to move to another random location saying if the snake head distance is less than 15
    # px of the food because food is 10 x 10 then the snake collided with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # tell it to increase score when the snake collides with food
        score.increase_score()

    # Detect collision with wall...basically saying if the snake head goes past these points
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    # [1:] is slicing which means not counting the head as a segment just the body and passing it to the
    # elif statement for the body segments saying if each segment of snake.head has a distance of less than 10 then
    # that is a collision...basically if head hits the body less than 10 in distance
    for segment in snake.all_snakes[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
