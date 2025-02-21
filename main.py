import turtle
import time
from snake import Snake
from foody import SnakeFood
from score import Score

sc = turtle.Screen()
sc.title("Snake game by Me")
sc.bgcolor('chartreuse1')
sc.setup(width=600, height=600)
sc.tracer(0)

half_width = (sc.window_width() / 2 ) + 0.4
half_height = (sc.window_height() / 2) - 1

snake = Snake()
food = SnakeFood()
score = Score()

sc.listen()
sc.onkey(fun=snake.go_up, key="Up")
sc.onkey(fun=snake.go_up, key="w")

sc.onkey(fun=snake.go_down, key="Down")
sc.onkey(fun=snake.go_down, key="s")

sc.onkey(fun=snake.go_left, key="Left")
sc.onkey(fun=snake.go_left, key="a")

sc.onkey(fun=snake.go_right, key="Right")
sc.onkey(fun=snake.go_right, key="d")

is_game_on = True

while is_game_on:
    sc.update()
    time.sleep(0.1)
    snake.move()


    # Detect collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.increaScore()

    # Detect collision with wall
    if snake.head.xcor() > half_width or snake.head.xcor() < -(half_width) or snake.head.ycor() > half_height or snake.head.ycor() < -(half_height):
        is_game_on = False
        score.gameOver()

    # Detect collision with the tail

    for segments in snake.snake_body[1:]:
        if snake.head.distance(segments) < 10:
            is_game_on = False
            score.gameOver()

sc.exitonclick()
