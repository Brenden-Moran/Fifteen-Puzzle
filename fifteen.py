# Author: Brenden Moran
# Date: 3/17/23

import random


class Fifteen:
    def __init__(self, size=4):
        self.size = size
        self.tiles = ([i for i in range(1, size ** 2)] + [0])   # Creates a list of tiles with numbers 0-15

    def draw(self):
        board = ""
        index = -1
        for x in range(self.size):          # Iterates through number 4 (size fo board
            for x in range(self.size):      # Iterates through 4 (size fo board)
                board += f'+---'            # Adds the top part of the board
            board += "+\n"                  # Finish adding the top part of the board
            for n in range(self.size):
                index += 1
                if self.tiles[index] < 10 and self.tiles[index] != 0:   # Checks if the number in the list of tiles
                    board += f'| {self.tiles[index]} '                  # is not a double-digit number
                elif self.tiles[index] == 0:                            # if so add a space before and after the
                    board += f'|   '                                    # number, else add space only after
                else:                                                   # if the number is 0 then make a blank space
                    board += f'|{self.tiles[index]} '
            board += "|\n"
        board += "+---+---+---+---+"                        # Add the bottom of the board once iteration is done
        return print(board)

    def __str__(self):
        string = ""
        for i in range(len(self.tiles)):        # Iterate through the number of tiles in the list
            if self.tiles[i] == 0:              # If the item of the tile corresponding to the index is equal
                string += "  "                  # to zero then make a blank space
            elif self.tiles[i] < 10:            # Add the character to the string
                string += f' {self.tiles[i]}'
            else:
                string += f' {self.tiles[i]}'
            if (i+1) % self.size == 0:          # If the index plus one is a multiple of 4 then add the new line
                string += " \n"                 # to the string
        return string

    def transpose(self, i, j):
        move_index = self.tiles.index(i)        # Move_index is the index of the move being done
        index_0 = self.tiles.index(j)           # Index_0 is the index of where 0 is located
        self.tiles[move_index] = j              # Swap each number in the tiles list that way I value is now J
        self.tiles[index_0] = i                 # and J value is now I
        return self.tiles

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        if move in self.tiles:                          # checks if the move is in the tiles list
            index = self.tiles.index(move)              # index is where the move is located in tiles
            if index+1 < 16 and ((index+1) % 4) != 0:   # if the index is within the range of the tiles and is not
                if self.tiles[index + 1] == 0:          # at the end of the board as well as next to it in tiles is 0
                    return True                         # then return True
            if index-1 > -1 and (index % 4) != 0:       # Checks the same thing as before but instead it checks behind
                if self.tiles[index-1] == 0:            # itself (to the left) of the move for 0
                    return True
            if index+self.size < 16:                    # if index + 4 is in the range of the tiles list and the index
                if self.tiles[index + self.size] == 0:  # corresponds with the item 0 then return true because 0 is
                    return True                         # located below the move
            if index-self.size > -1:                    # Checks the same thing as before but if true then the move is
                if self.tiles[index-self.size] == 0:    # above 0
                    return True
        return False                                    # If all checks fail then return False (not a valid move)

    def update(self, move):
        if Fifteen.is_valid_move(self, move):           # checks if the move given is valid
            return Fifteen.transpose(self, move, 0)     # if True then exchange the move with 0
        else:
            return print("This is not a valid move")    # if not then tell the user that it is not a valid move

    def shuffle(self, moves=100):
        while moves > 0:                    # iterate while moves are greater than 0
            moves -= 1
            possible_moves = []             # creates possible_move as an empty list
            index = self.tiles.index(0)     # Index is the index of 0 in the list tiles
            if index+1 < 16 and ((index+1) % 4) != 0:           # This goes through the same steps as the checking
                possible_moves.append(self.tiles[index+1])      # (is_valid_move) function only if it has found a
            if index-1 > -1 and (index % 4) != 0:               # valid move then add it to the list of possible
                possible_moves.append(self.tiles[index-1])      # moves
            if index+self.size < 16:
                possible_moves.append(self.tiles[index+self.size])
            if index-self.size > -1:
                possible_moves.append(self.tiles[index-self.size])
            move = random.choice(possible_moves)                # make move a random choice from the list of possible
            Fifteen.update(self, move)                          # moves and updated the board

    def is_solved(self):
        tiles_test = ([i for i in range(1, self.size ** 2)] + [0])
        if tiles_test == self.tiles:            # If the tiles match with the tiles of the board then
            return True                         # return True
        else:
            return False                        # otherwise return False

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle (optional)
    def solve(self):
        pass

if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n 13 14 15   \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n 13 14   15 \n'
    game.update(15)
    assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n 13 14 15   \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n 13 14 15   \n'
    assert game.is_solved() == False
    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

