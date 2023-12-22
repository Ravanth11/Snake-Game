from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen1 = Screen()
screen1.title("Snake Game")
screen1.setup(600,600)
screen1.bgcolor("black")

snake = Snake()
food1 = Food()
scoreboard = Scoreboard()

screen1.listen()
screen1.onkey(snake.up,"Up")

screen1.onkey(snake.down,"Down")

screen1.onkey(snake.left,"Left")

screen1.onkey(snake.right,"Right")



game_is_on = True

while game_is_on:
    snake.mov()

    if snake.head().distance(food1)<15:
        food1.refresh()
        scoreboard.scoreupdate()
        
    if (
    snake.head().xcor() > 280
    or snake.head().ycor() > 280
    or snake.head().xcor() < -280
    or snake.head().ycor() < -280
    ):
        
        game_is_on = False
        t1 = Turtle()
        t1.hideturtle()
        t1.color("white")
        t1.write("GAME OVER" , align = "center" , font = ("Arial,24,normal"))



screen1.exitonclick()