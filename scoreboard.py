from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

screen = Screen()
user_name = screen.textinput("Name", "Enter your name: ")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()


    def user_input(self):
        self.goto(x=0, y=-50)
        self.write(f"{user_name}", align=ALIGNMENT, font=FONT)



    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def total_score(self):
        self.goto(x=0, y=-100)
        if self.score == 1:
            self.write(f"You scored: {self.score} point", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"You scored: {self.score} points", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



