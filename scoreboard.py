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
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # telling player that game is over
    def game_over(self):
        # goto to put "Game Over" in the middle of the screen when the player hits the wall
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    # defining increase score so the score can add 1 when it collides with food, clear the previous score and write
    # new score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


