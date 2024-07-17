from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.ht()
        self.goto(-235, 260)
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

    def update_level(self):
        self.level += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)