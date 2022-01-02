from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 25, "normal",)

class Comment(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(5.0, 240.0)

    def print_turn(self, player):
        self.clear()
        self.write(arg=f"{player.name}'s turn", font=FONT, align=ALIGNMENT)

    def moves_up(self, player, move_len):
        self.clear()
        self.write(arg=f"{player.name} moves up by {move_len} boxes.", font=FONT, align=ALIGNMENT)

    def player_won(self, player):
        self.clear()
        self.write(arg=f"{player.name} won!", font=FONT, align=ALIGNMENT)

    def snake(self, player):
        self.clear()
        self.write(arg=f"{player.name} got eaten by snake!", font=FONT, align=ALIGNMENT)
    def ladder(self, player):
        self.clear()
        self.write(arg=f"{player.name} climbed up a ladder!!", font=FONT, align=ALIGNMENT)
        