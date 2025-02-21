from turtle import Turtle

class Score(Turtle):

  def __init__(self):
    super().__init__()
    self.scoree = 0
    self.hideturtle()
    self.updateScore()
  
  def updateScore(self):
    """Updates the score everytime when snake hits the ball"""

    self.clear()
    self.penup()
    self.goto(0, 265)
    self.write(f"Score: {self.scoree}", align="center", font=("Courier", 24, "normal"))

  def increaScore(self):
    """Increases the score whne snakes eats the ball"""

    self.scoree += 1
    self.updateScore()

  def gameOver(self):
    """Pups up when the game is over"""

    self.goto(0, 0)
    self.hideturtle()
    self.color("white")
    self.write(f"Game is Over", align="center", font=("Georgia", 22, "normal"))