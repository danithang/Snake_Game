from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


# defining a class to keep score, making sure score goes to top (with goto) center and the color can be seen
# identifying that the score is zero at first and writing it as such
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.score = 0
        # reading the input in data.txt into the game for the high score
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    # updating scoreboard with score and high score to beat
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # defining reset if current score gets higher than high score then the current score will become the new high score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # telling the game that the high score needs to write to the game so the high score will show everytime the game opens
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        # resetting the score to 0 if the if statement above doesn't get triggered
        self.score = 0
        self.update_scoreboard()

    # defining increase score so the score can add 1 when it collides with food, clear the previous score and write
    # new score
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


