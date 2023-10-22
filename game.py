# Author: Brenden Moran
# Date: 3/17/23

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice


def shuffle(count, num):
    if num > count:
        possible_moves = []                                 # Possible_moves is an empty list
        empty = board.tiles.index(0)                        # Creates empty as the index for where 0 is located
        if empty + 1 < 16 and ((empty+1) % 4) != 0:         # goes through the same checks as in Fifteen to see
            possible_moves.append(board.tiles[empty + 1])   # if the move is a possible move
        if empty - 1 > -1 and (empty % 4) != 0:             # if the move is possible then add it to the possible moves
            possible_moves.append(board.tiles[empty - 1])   # list
        if empty + board.size < 16:
            possible_moves.append(board.tiles[empty + board.size])
        if empty - board.size > -1:
            possible_moves.append(board.tiles[empty - board.size])
        move = choice(possible_moves)                       # randomly select a move from the possible moves list
        index = board.tiles.index(move)                     # index is the index of the random move
        list_tiles[empty].set(move)                         # edit the list of tiles index where 0 is located with the
        list_tiles[index].set(" ")                          # move and edit the index where move is located with a
        gui.nametowidget(index).configure(bg="white")       # blank
        gui.nametowidget(empty).configure(bg="red")         # Change the background colors of the squares as well
        board.update(move)                                  # update the board's state
        gui.after(300, lambda: shuffle(count + 1, num))     # Recursively call on the shuffle function and increment
                                                            # The count number up by 1
def click_button(value, pos):
    global board, list_tiles
    if pos == 16:                                       # if the position in the tiles is 16 then that is the shuffle
        shuffle(1, 30)                                  # button and it will run the shuffle function
    elif board.is_valid_move(board.tiles[pos]):         # if the move is valid for the button which the user pressed
        empty = board.tiles.index(0)                    # then update the board's state
        list_tiles[empty].set(board.tiles[pos])
        list_tiles[pos].set(" ")                        # change the values of the move as well as where the 0 is
        gui.nametowidget(pos).configure(bg="white")     # located
        gui.nametowidget(empty).configure(bg="red")     # edit the background colors of the move and blank space as well
        board.update(board.tiles[pos])                  # update board's state
    return list_tiles, board.tiles


def add_button(gui, pos, value): # value is a tile label and pos a tile position on the board
    if pos == 16:           # if the position is 16 then that is the shuffle button
        return Button(gui, textvariable=value, name=str(pos), bg="white", fg='black',
                      font=font1, height=1, width=10,
                      command=lambda: click_button(value, pos))     # Creates shuffle button and binds to click button
    elif board.tiles[pos] == 0: # if the position is 0 then that is the blank space
        return Button(gui, textvariable=value, name=str(pos), bg="white", fg='black',
                      font=font1, height=2, width=5,
                      command=lambda: click_button(value, pos)) # Creates the button for the blank space
    else:                                                       # And binds to click button function
        return Button(gui, textvariable=value, name=str(pos), bg="red", fg='black',
        font=font1, height=2, width=5,
        command = lambda: click_button(value, pos))     # Makes buttons for all the other spaces and binds them to
                                                        # the click button function

if __name__ == '__main__':
    # make tiles
    board = Fifteen()
    list_tiles = []

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    for i in board.tiles:
        value = StringVar()             # Adds the StringVar value of each value in the list of tiles
        if i == 0:
            value.set(" ")              # making sure 0 is a blank space
        else:
            value.set(i)
        list_tiles.append(value)        # then appends that value to list_tiles

    font1 = font.Font(family='Helveca', size='25', weight='bold')       # Sets font size

    shuffle_val = StringVar()
    shuffle_val.set("Shuffle")
    shuffle_button = add_button(gui, 16, shuffle_val)       # Sets the shuffle buttons value

    b0 = add_button(gui, 15, (list_tiles[15]))              # creates each button for the game by calling on
    b1 = add_button(gui, 0, (list_tiles[0]))                # the add_button function
    b2 = add_button(gui, 1, (list_tiles[1]))
    b3 = add_button(gui, 2, (list_tiles[2]))
    b4 = add_button(gui, 3, (list_tiles[3]))
    b5 = add_button(gui, 4, (list_tiles[4]))
    b6 = add_button(gui, 5, (list_tiles[5]))
    b7 = add_button(gui, 6, (list_tiles[6]))
    b8 = add_button(gui, 7, (list_tiles[7]))
    b9 = add_button(gui, 8, (list_tiles[8]))
    b10 = add_button(gui, 9, (list_tiles[9]))
    b11 = add_button(gui, 10, (list_tiles[10]))
    b12 = add_button(gui, 11, (list_tiles[11]))
    b13 = add_button(gui, 12, (list_tiles[12]))
    b14 = add_button(gui, 13, (list_tiles[13]))
    b15 = add_button(gui, 14, (list_tiles[14]))

    # add buttons to the grid
    buttons = [b1, b2, b3, b4,
               b5, b6, b7, b8,
               b9, b10, b11, b12,
               b13, b14, b15, b0]
    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i * k + j].grid(row=i + 1, column=j, columnspan=1)      # sets up the board using the .grid()
    shuffle_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)    # function

    gui.mainloop()
