import turtle
import pandas as pd
from die import Die
from player import Player
from comment import Comment
import time
import snake_data
import ladder_data

# the main screen where our board is displayed
game_screen = turtle.Screen()
game_screen.title("Snakes and Ladders")

# the game board image
image = "graphic/game_screen.gif"

# adding the image as a shape
turtle.addshape(image)
turtle.shape(image)

# asking for player names 
name_1 = turtle.textinput(title="Enter Name", prompt="Enter name of player 1.")
name_2 = turtle.textinput(title="Enter Name", prompt="Enter name of player 2.")

# initialisation of some objects :-----------------------------------
die = Die()
player_1 = Player(-229.0, -150.0, "green", name_1) # the first player
player_2 = Player(-226.0, -200.0, "blue", name_2) # the second player
comment_bar = Comment()
# -------------------------------------------------------------------

# the coordinates of the numbered boxes
# extracting using pandas
box_data = pd.read_csv("./data/box_pos.csv")

# storing the x and y coordinates in their own lists
# they are of type pandas Series and must be converted to int
box_x_cors = box_data["x"].to_list()
box_y_cors = box_data["y"].to_list()

# GAME LOGIC-------------------------------------------------------------------
current_player = player_1
comment_bar.print_turn(current_player)
game_is_on = True

def move_piece(current_location, destination, snake=False, ladder=False):
    move = destination - current_location
    if snake:
        comment_bar.snake(current_player)
        time.sleep(2)
    elif ladder:
        comment_bar.ladder(current_player)
        time.sleep(2)
    else:
        comment_bar.moves_up(current_player, move)
    current_player.move_anim(box_x_cors[destination], box_y_cors[destination])
    current_player.location = destination

def change_current_player():
    global current_player
    if current_player == player_1:
        current_player = player_2
    elif current_player == player_2:
        current_player = player_1

def move_process():
    global game_is_on
    pieces_moving = True
    current_location = current_player.location
    destination = current_location + die.play_roll_anim()
    if not game_is_on:
        return
    if current_player.is_out:
        if len(box_x_cors) - 1 < destination:
            pass
        else:
            move_piece(current_location, destination)
            print("shit moved #1")
            time.sleep(2.5)
    else:
        if destination == 1:
            move_piece(current_location, destination)
            print("shit moved #2")
            time.sleep(3)
            current_player.is_out = True
    
    if current_player.location in snake_data.snakes:
        destination = snake_data.snakes[current_player.location]
        move_piece(current_location, destination, snake=True)

    elif current_player.location in ladder_data.ladders:
        destination = ladder_data.ladders[current_player.location]
        move_piece(current_location, destination, ladder=True)

    elif current_player.location == 29:
        comment_bar.player_won(current_player)
        game_is_on = False
        return

    print(f"{current_player.name}'s location is {current_player.location}")
    change_current_player()
    comment_bar.print_turn(current_player)

game_screen.listen()
game_screen.onkey(move_process, "space")
# -------------------------------------------------------------------------------
# FIND COORDINATES ON SCREEN
# def get_mouse_click_coor(x, y):
#     turtle.onscreenclick(None)
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# --------------------------------------------------------------------------------

turtle.mainloop()