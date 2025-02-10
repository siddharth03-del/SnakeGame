from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
snake = Snake()
screen = Screen()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake.create_snake()
food = Food()
score.updates_scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_move, 'Left')
screen.onkey(snake.right_move, 'Right')
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290 :
        game_is_on = False
        score.game_over()
    if snake.segments[0].distance(food) < 15:
        score.updates_scoreboard()
        snake.extend()
        food.fresh_food()
    for i in range(1, len(snake.segments)):
        if snake.segments[0].distance(snake.segments[i]) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
