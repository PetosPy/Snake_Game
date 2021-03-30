
from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
pet = Turtle(shape="turtle")
pet.speed(1)
screen.listen()

directions = [0, 90, 180, 270]

screen.bgcolor("black")
screen.title("Petos the Snake ")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reseter()
        snake.snake_reset()
        #scoreboard.user_input()
        #scoreboard.total_score()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reseter()
            snake.snake_reset()
            #scoreboard.user_input()
            #scoreboard.total_score()











screen.exitonclick()


