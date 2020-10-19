"""

@author Julian
@date Fall 2020

Command line game to play tic-tac-toe against a simple computer bot. 
User selects X or O, takes turns adding their move to the board, 
and the script detects and announces a winner or draw.

"""


import random
import time

class Board:

    def __init__(self, dimension):
        self.dimension = dimension
        self.locations = [*range(1, self.size()+1)]
        self.valid_moves = [*range(1, self.size()+1)]
        self.values = [0]*9
        self.visuals = [" "]*9

    def row_as_str(self, row_number, list_type):
        start = (row_number-1)*self.dimension
        return(" | ".join(map(str,list_type[start:start+self.dimension])))


    def print(self,list_type):
        for i in range(1,self.dimension):
            print(self.row_as_str(i,list_type))
            print("---------")
        print(self.row_as_str(self.dimension,list_type))

    

    def check_win(self):
        for i in range(0,self.dimension):
            # check rows
            if abs(sum(self.values[(i*self.dimension):(i+ self.dimension)])) == self.dimension:
                return True
            # check cols
            elif abs(sum(self.values[i:(self.size()):self.dimension])) == self.dimension:
                return True
        # check diagonals
        return((abs(self.values[0]+ self.values[4]+ self.values[8]) == 3) | 
                (abs(self.values[2]+ self.values[4]+ self.values[6]) == 3) )


    def is_legal_move(self, location):
        return( (location != None) and
                (location >= 0) and
                (location <= self.size()) and 
                (self.values[location-1] == 0 ))


    def add_move(self, location, move, num_moves):
        self.values[location-1] = (move == "X") - (move == "O")
        self.locations[location-1] = move
        self.visuals[location-1] = move
        self.valid_moves.remove(location)

    def size(self):
        return( self.dimension * self.dimension)

    def min_winning_moves(self):
        return (self.dimension + self.dimension - 1)

    def random_move(self):
        return( self.valid_moves[random.randint(0,len(self.valid_moves)-1)])

def user_pick_move(board):
    choice = None
    attempts = 0
    while not (board.is_legal_move(choice)) :
        attempts = attempts + 1
        if(attempts > 1):
            print("Available Moves:")
            board.print(board.locations)
        try:
            choice = int(input("Which square" + str(board.valid_moves) + "?\n"))

        except ValueError:
            pass
    return choice

def computer_pick_move(board):
    return(board.random_move())

def alternate_move(last_move):
    if last_move == "O":
        return "X"
    else:
        return "O"

def play_game(board, user_move, computer_move):

    last_move = "O"
    num_moves = 0
    board.print(board.locations)

    while num_moves<=board.size(): 
        if last_move == computer_move:
            # if computer went last or its first turn, user goes
            board.add_move(user_pick_move(board), user_move, num_moves)
        else:
            print("Computer thinking...")
            time.sleep(1)
            board.add_move(computer_pick_move(board), computer_move, num_moves)
        last_move = alternate_move(last_move)
        num_moves = num_moves + 1
        board.print(board.visuals)
        if (num_moves>=board.min_winning_moves() and board.check_win()):
            if(last_move == computer_move):
                print("You lost!")
                return -1
            else:
                print("You won!")
                return 1
    print("Tie!")
    return 0


if __name__ == "__main__":
    dimension = 3
    board = Board(dimension)
    choice = None
    while choice not in ["X","O"]:
       try:
          choice = str(input("Do you want to be \'X\' or \'O\' ? \n")).upper()
       except ValueError:
          pass
    if choice == "X":
        play_game(board, "X","O")
    else: 
        play_game(board, "O","X")
    
  