import turtle

STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVING_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_body = []
        self.current_direction = 'stop'
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            snake = turtle.Turtle()
            snake.shape("square")
            snake.color('black')
            snake.penup()
            snake.goto(i)
            self.snake_body.append(snake)

    def go_up(self):
        if self.current_direction != 'down':
            self.current_direction = 'up'

    def go_down(self):
        if self.current_direction != 'up':
            self.current_direction = 'down'

    def go_right(self):
        if self.current_direction != 'left':
            self.current_direction = 'right'

    def go_left(self):
        if self.current_direction != 'right':
            self.current_direction = 'left'

    def move(self):
        if self.current_direction != 'stop':
            for seg_num in range(len(self.snake_body) - 1, 0, -1):
                new_xp = self.snake_body[seg_num - 1].xcor()
                new_yp = self.snake_body[seg_num - 1].ycor()
                self.snake_body[seg_num].goto(new_xp, new_yp)

            self.head.forward(MOVING_DISTANCE)

        if self.current_direction == "up":
            self.head.setheading(90)
        elif self.current_direction == "down":
            self.head.setheading(270)
        elif self.current_direction == "left":
            self.head.setheading(180)
        elif self.current_direction == "right":
            self.head.setheading(0)