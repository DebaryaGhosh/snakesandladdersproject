from turtle import Turtle
import turtle 

counter_sprite_1 = "./graphic/counter_1.gif"
counter_sprite_2 = "./graphic/counter_2.gif"
turtle.addshape(counter_sprite_1)
turtle.addshape(counter_sprite_2)

class Player(Turtle):
    def __init__(self, x_pos, y_pos, name, sprite):
        super().__init__()
        if sprite == 1:
            self.shape(counter_sprite_1)
        elif sprite == 2:
            self.shape(counter_sprite_2)
        self.penup()
        self.goto(x_pos, y_pos)
        self.location = 0
        self.is_out = False
        self.name = name

    def move_anim(self, x_cor_list, y_cor_list):
        self.goto(int(x_cor_list), int(y_cor_list))
