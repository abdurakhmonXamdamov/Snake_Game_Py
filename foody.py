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
        self.blinking = True 
        self.blink()
        self.change_Color()

    def refresh(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)

    def blink(self):
        if not self.blinking:
            return  
        if self.isvisible():
            self.hideturtle()
        else:
            self.showturtle()
        self.screen.ontimer(self.blink, 350)

    def change_Color(self):
        self.color(random.choice(self.color_tank))

    def destroy(self):
        self.blinking = False  
        self.hideturtle()
