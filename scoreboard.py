from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
    def updates_scoreboard(self):
        self.goto(0,270)
        self.color('white')
        self.clear()
        self.score += 1
        self.write("Score : " + str(self.score), align='center', font=('Arial', 15 , 'bold') )
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", align='center', font=('Arial', 24, 'bold'))