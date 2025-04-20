import turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

class Snaky:
    def __init__(self, score_class):
        self.score = score_class
        self.snake_body_parts = []
        self.current_pos  = 'stop'
        self.snake_speed = 0.12
        self.create_snake()
        self.head = self.snake_body_parts[0]


    def add_segment(self, position):
        """
        this funct creates snake shapes
        :param position: here comes the START POSITIONS
        :return: no return value
        """
        snake_make = turtle.Turtle('square')
        snake_make.color('black')
        snake_make.penup()
        snake_make.goto(position)
        self.snake_body_parts.append(snake_make)

    def create_snake(self):
        """
        this func combines all snake shapes and create one whole snake in a default size 3
        :return: no return value
        """
        for i in START_POSITIONS:
            self.add_segment(i)

    def extend(self):
        self.add_segment(self.snake_body_parts[-1].position())

    def increase_speed(self):
        if self.snake_speed > 0.04:
            self.snake_speed -= 0.01



    def go_up(self):
        """
        this func moves snake upward
        :return:
        """
        if self.current_pos != 'down':
            self.current_pos = 'up'

    def go_down(self):
        """
        this func moves snake downward
        :return:
        """
        if self.current_pos != 'up':
            self.current_pos = 'down'

    def go_right(self):
        """
        this one moves snake rightward
        :return:
        """
        if self.current_pos != 'left':
            self.current_pos = 'right'

    def go_left(self):
        """
        this one moves snake leftward
        :return:
        """
        if self.current_pos != 'right':
            self.current_pos = 'left'

    def move(self):
        """
        this func first checks the current position of the snake and according to that info it confirms where
        snake goes up, down, right, left
        :return:
        """
        if self.current_pos != 'stop':
            for seg_num in range(len(self.snake_body_parts) - 1, 0, -1):
                new_x = self.snake_body_parts[seg_num - 1].xcor()
                new_y = self.snake_body_parts[seg_num - 1].ycor()
                self.snake_body_parts[seg_num].goto(new_x, new_y)

            self.head.forward(MOVING_DISTANCE)

        if self.current_pos == 'up':
            self.head.setheading(90)
        elif self.current_pos == 'down':
            self.head.setheading(270)
        elif self.current_pos == 'right':
            self.head.setheading(0)
        elif self.current_pos == 'left':
            self.head.setheading(180)

    def freeze(self):
        self.score.is_paused = True

    def unfreeze(self):
        self.score.is_paused = False
    
    def reset_snake(self):
        for segment in self.snake_body_parts:
            segment.goto(1000, 1000)  
        self.snake_body_parts.clear()
        self.create_snake()
        self.head = self.snake_body_parts[0]
        self.snake_speed = 0.12

    def destroy(self):
        for segment in self.snake_body_parts:
            segment.hideturtle()
        self.snake_body_parts.clear()
