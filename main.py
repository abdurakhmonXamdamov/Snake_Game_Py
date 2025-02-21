import turtle
import time
from snake import Snake

sc = turtle.Screen()
sc.title("Snake game by Me")
sc.bgcolor('chartreuse1')
sc.setup(width=600, height=600)
sc.tracer(0)

snake = Snake()

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

sc.exitonclick()
