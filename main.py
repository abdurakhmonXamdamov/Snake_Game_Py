import turtle
import time
from snake import Snaky
from foody import SnakeFood
from score import Score

sc = turtle.Screen()
sc.title("Snake game by Me")
sc.bgcolor('DodgerBlue4')
sc.setup(width=600, height=600)
sc.tracer(0)

half_width = (sc.window_width() / 2 )
half_height = (sc.window_height() / 2)

food = SnakeFood()
score = Score()
snake = Snaky(score)

sc.listen()
sc.onkey(fun=snake.go_up, key="Up")
sc.onkey(fun=snake.go_up, key="w")

sc.onkey(fun=snake.go_down, key="Down")
sc.onkey(fun=snake.go_down, key="s")

sc.onkey(fun=snake.go_left, key="Left")
sc.onkey(fun=snake.go_left, key="a")

sc.onkey(fun=snake.go_right, key="Right")
sc.onkey(fun=snake.go_right, key="d")

sc.onkey(fun=snake.freeze, key="p")
sc.onkey(fun=snake.unfreeze, key="r")

is_game_on = True

while is_game_on:
    sc.update()
    time.sleep(snake.snake_speed)

    if not score.is_paused:
        snake.move()
        score.game_resumed()
    else:
        score.game_paused()

    # Detect collision with food 
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.increaseScore()
        food.change_Color()

        if score.scoree % 3 == 0:
            snake.increase_speed()

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -half_width or
            int(snake.head.ycor()) > half_height or snake.head.ycor() < -290):
        is_game_on = False
        score.game_over()

    # Detect collision with the tail
    for segments in snake.snake_body_parts[1:]:
        if snake.head.distance(segments) < 10:
            is_game_on = False
            score.game_over()


sc.mainloop()
