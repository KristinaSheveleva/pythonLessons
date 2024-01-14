from turtle import Turtle, Screen
import time 
from snake import Snake
from snake_food import Food
from snake_score import Score

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.update_food()
        score.increase_score()
        snake.long_snake()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()
    for segments in snake.segments[1:]:
            if snake.head.distance(segments)<10:
                game_is_on=False
                score.game_over()    
                 
                 



    
    

screen.exitonclick()




