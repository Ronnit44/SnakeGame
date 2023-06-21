from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
# from pseudofood import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
# pseudofood = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")



game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()
    #detecting collisions with food and increasing the score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detecting collisions with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    #detecting collision between head and tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()