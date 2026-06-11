from turtle import Turtle
import datetime
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE_PATH = os.getcwd() 
FILE_NAME = "/highscore.txt"
FULL_PATH = FILE_PATH + FILE_NAME

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.speed("fastest")
        self.up()
        self.hideturtle()
        self.goto(-20, 260)
        self.color("white")
        self.refresh()
        
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.save_highscore()
            self.highscore = self.score
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1

    def read_highscore(self):
        with open(FULL_PATH) as file:
            last_line = file.readlines()[-1]
            self.highscore = int(last_line.split()[1])
            

    def save_highscore(self):
        with open(FULL_PATH, "a") as f:
            now = datetime.datetime.now()
            now_format = now.strftime("%Y-%m-%d %H:%M")
            f.write(f"\nWynik: {self.score} Data: {now_format}")
            f.close()  