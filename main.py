from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_on = False

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
