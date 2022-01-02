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
player_1 = Player(-229.0, -150.0, name_1, 1) # the first player
player_2 = Player(-226.0, -200.0, name_2, 2) # the second player
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
comment_bar.print_turn(current_player) # prints the name of the player who has the current turn

# a flag which, when false, doesn't allow the player to play anymore.
game_is_on = True

# involved in moving the pieces on board
def move_piece(current_location, destination, snake=False, ladder=False):
    # calculates the amount of boxes the counter moves
    move = destination - current_location 

    # if the player was swallowed by snake...
    if snake:
        comment_bar.snake(current_player) # prints suitable message
        time.sleep(2)
    # if the player climbed up a ladder...
    elif ladder:
        comment_bar.ladder(current_player)
        time.sleep(2)
    else:
        comment_bar.moves_up(current_player, move)

    # plays the animation of the counter moving from current_location to destination
    current_player.move_anim(box_x_cors[destination], box_y_cors[destination])

    # location of the current player is set to destination
    current_player.location = destination

def change_current_player():
    # changes the current player after every turn
    global current_player
    if current_player == player_1:
        current_player = player_2
    elif current_player == player_2:
        current_player = player_1

def move_process():
    game_screen.onkey(None, 'space')
    global game_is_on 
    # current location of the player is set...
    current_location = current_player.location
    # ...and destination is calculated depending on the return of dice.play_roll_anim()
    # it returns an integer which is the number of boxes the player will go up
    destination = current_location + die.play_roll_anim()
    # if game is not on, then no movement will occur. The function will return
    if not game_is_on:
        return
    # if current player is out...
    if current_player.is_out:
        # if the number on dice is more than the required amount to reach the end
        # then no movement will occur
        if len(box_x_cors) - 1 < destination:
            pass
        # otherwise counter will move by the required amount
        else:
            move_piece(current_location, destination)
            time.sleep(2.5)
    # if player is NOT out from the first box yet,
    else:
        # if the number on dice is 1, then piece will move out
        if destination == 1:
            move_piece(current_location, destination)
            time.sleep(3)
            current_player.is_out = True
    
    # if the location of a player is on a box which has snake mouth on it...
    if current_player.location in snake_data.snakes:
        # ...then destination is set to the end of the tail of the snake
        destination = snake_data.snakes[current_player.location]
        # and the player is moved to the destination.
        move_piece(current_location, destination, snake=True)
    
    # if the location of a player is on a box which has the end of a ladder on it...
    elif current_player.location in ladder_data.ladders:
        # the destination is set to the top of the ladder
        destination = ladder_data.ladders[current_player.location]
        # and the player is, hence, moved to te destination
        move_piece(current_location, destination, ladder=True)

    # if the player is on the last box (30, of index 29)...
    elif current_player.location == 29:
        # comment bar prints that the current player won the game
        comment_bar.player_won(current_player)
        # and the game is turned off
        game_is_on = False
        return

    # changes the current player after their turn
    change_current_player()
    # prints the name of the current player
    comment_bar.print_turn(current_player)
    game_screen.onkey(move_process, "space")

# listens for user input
game_screen.listen()
game_screen.onkey(move_process, "space")

turtle.mainloop()