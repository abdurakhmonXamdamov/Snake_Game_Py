import turtle
import random

class SnakeFood(turtle.Turtle):

  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    self.shapesize(stretch_len=0.7, stretch_wid=0.7)
    self.color_tank = ["firebrick2", "green3", "black", "DimGrey", "red1", "SpringGreen1", "blue1", "chocolate",
                       "purple2", "snow", "yellow", "VioletRed", "sienna"]
    self.speed('fastest')
    self.refresh()
    self.blink()
    self.change_Color()

  def refresh(self):
    """Move the food to a new random Location"""

    random_x = random.randint(-290, 290)
    random_y = random.randint(-290, 290)
    self.goto(random_x, random_y)



  def blink(self):
        """Make the food blink (appear and disappear)"""

        if self.isvisible():
            self.hideturtle() 
        else:
            self.showturtle()  

        self.screen.ontimer(self.blink, 350)


  def change_Color(self):
      """Change the color of the food to a random color from the color tank"""
      self.color(random.choice(self.color_tank))
