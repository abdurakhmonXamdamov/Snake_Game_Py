import turtle

import random

class SnakeFood(turtle.Turtle):

  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    self.shapesize(stretch_len=0.7, stretch_wid=0.7)
    self.color("firebrick2")
    self.speed('fastest')
    screen = turtle.Screen()
    self.width = screen.window_width()
    self.height = screen.window_height()
    self.refresh()
    self.blink()

  def refresh(self):
    """Move the food to a new random Location"""

    random_x = random.randint(-int(self.width / 2), int(self.width / 2))
    random_y = random.randint(-int(self.height / 2), int(self.height / 2))
    self.goto(random_x - 20, random_y - 20)

  def blink(self):
        """Make the food blink (appear and disappear)"""

        if self.isvisible():
            self.hideturtle() 
        else:
            self.showturtle()  

        self.screen.ontimer(self.blink, 350)