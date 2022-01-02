import turtle
from turtle import Turtle
import random
import time

# dice graphics
SPRITE_1 = "./graphic/die_1.gif"
SPRITE_2 = "./graphic/die_2.gif"
SPRITE_3 = "./graphic/die_3.gif"
SPRITE_4 = "./graphic/die_4.gif"
SPRITE_5 = "./graphic/die_5.gif"
SPRITE_6 = "./graphic/die_6.gif"
turtle.addshape(SPRITE_1)
turtle.addshape(SPRITE_2)
turtle.addshape(SPRITE_3)
turtle.addshape(SPRITE_4)
turtle.addshape(SPRITE_5)
turtle.addshape(SPRITE_6)


# list of frames to play animation from
ANIM_LIST = [SPRITE_1, SPRITE_2, SPRITE_3, SPRITE_4, SPRITE_5, SPRITE_6]
ANIM_DURATION = 15 # length of animation

class Die(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SPRITE_1)
        self.penup()
        self.speed("fastest")
        self.goto(x=-291.0, y=255.0) # default position of dice
    
    def play_roll_anim(self):
        anim_dur = 0
        while anim_dur < ANIM_DURATION:
            time.sleep(0.05) # time between frames
            anim_dur += 1
            change_graphic_to = random.choice(ANIM_LIST) # random frame from ANIM_LIST
            self.shape(change_graphic_to) # change image to current frame
        anim_dur = 0 # after animation, back to default value (0)
        return ANIM_LIST.index(change_graphic_to) + 1
        