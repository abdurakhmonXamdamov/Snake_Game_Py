from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoree = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.is_paused = False 

        self.message_turtle = Turtle()
        self.message_turtle.hideturtle()
        self.message_turtle.color("white")
        self.message_turtle.penup()

        with open("snake_score_recorder.txt", "r") as sk:
            self.high_score = int(sk.read())

        self.update_score()


    def update_score(self):
        """Updates the score every time the snake hits the ball"""

        if self.scoree > self.high_score:
          self.high_score = self.scoree

        with open("snake_score_recorder.txt", "w") as sk:
            sk.write(str(self.high_score))

        self.clear()
        self.write("Score: {}   High Score: {}".format(self.scoree, self.high_score), align="center",
                    font=("Courier", 24, "normal"))

    def increaseScore(self):
        """Increases the score when the snake eats the ball"""
        self.scoree += 1
        self.update_score()

    def game_over(self):
        """Shows 'Game Over'"""
        self.message_turtle.clear()
        self.message_turtle.goto(0, 0)
        self.message_turtle.write("Game is Over", align="center", font=("Courier", 22, "normal"))

    def game_paused(self):
        """Shows 'Paused' if paused"""
        self.message_turtle.clear()
        if self.is_paused:
            self.message_turtle.goto(0, 0)
            self.message_turtle.write("Paused", align="center", font=("Courier", 22, "normal"))

    def game_resumed(self):
        """Clears pause message on resume"""
        self.message_turtle.clear()

    def destroy(self):
        self.clear()
        self.hideturtle()
        self.message_turtle.clear()
        self.message_turtle.hideturtle()

