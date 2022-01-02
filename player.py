from turtle import Turtle

# -229.0, -150.0
# -226.0 -200.0
class Player(Turtle):
    def __init__(self, x_pos, y_pos, color, name):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.goto(x_pos, y_pos)
        self.location = 0
        self.is_out = False
        self.name = name

    def move_anim(self, x_cor_list, y_cor_list):
        # print(x_cor_list)
        # print(y_cor_list)
        # print("\n\n")
        self.goto(int(x_cor_list), int(y_cor_list))
