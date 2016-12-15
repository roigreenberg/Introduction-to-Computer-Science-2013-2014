#############################################################
# FILE: battleship.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex4 2013-2014
# Description: execute Battleship game. create a board, place
# ships and fire on the ships and try do desrtoy them
#############################################################

def ship_index(board):
    """find the highest ship index on board

    Args:
    -board: battleshipe board - you can assume its legal

    return: the next ship-index."""
    
    index = 0
    # scaning the board for ships and remember the highest value
    for wid in range(len(board[0])):
        for heig in range(len(board)):
            if board[heig][wid] is not None: # if ship found, take the higher index
                index = max(index, board[heig][wid][0])
    return (index + 1)



def new_board(width=10,height="height"):
    """creates a new board game for a Battleship game.

    Args:
    -width: a positive int - the width of the board - default value 10
    -height: a positive int - the height of the board - if not spcified
    should be as width

    return: a NEW enpty board - each inner arrays is a list of 'None's.

    n case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    
    if height=="height": # if no height given, give the width value
        height = width

    # verifies the input
    if height <=0 or width <= 0:
        return
    # create the board
    board =[]
    for heig in range(height):  # rows
        board.append([])
        for wid in range(width):  # lines
            board[heig].append(None)
    return board

def place_ship(board,ship_length,bow,ship_direction):
    """Put a new ship on the board

    put a new ship (with unique index) on the board.
    in case of successful placing edit the board according to the definitions
    in the ex description.

    Args:
    -board - battleshipe board - you can assume its legal
    -ship_length: a positive int the length of the ship
    -bow: a tuple of ints the index of the ship's bow
    -ship_direction: a tuple of ints representing the direction the ship
    is facing (dx,dy) - should be out of the 4 options(E,N,W,S):
    (1,0) -facing east, rest of ship is to west of bow,
    (0,-1) - facing north, rest of ship is to south of bow, and etc.

    return: the index of the placed ship, if the placement was successful,
    and 'None' otherwise.

    In case of bad input: values are out of range returns None

     You can assume the board is legal. You can assume the other inputs
     are of the right form. You need to check that they are legal."""

    # verifies the input
    if abs(ship_direction[0])+abs(ship_direction[1])==1 and \
       0 <= bow[0] < len(board[0]) and 0 <= bow[1] < len(board) and \
       -1 <= (bow[0] - ship_direction[0]*ship_length) <= len(board[0]) and \
       -1 <= (bow[1] - ship_direction[1]*ship_length) <= len(board):

        index=ship_index(board)  # find the next ship-index
        size=[ship_length]
        for part in range(ship_length):  # try to place the ship
            if board[bow[1]-ship_direction[1]*part]\
               [bow[0]-ship_direction[0]*part] == None:
                board[bow[1]-ship_direction[1]*part]\
                     [bow[0]-ship_direction[0]*part]  = (index, part, size)
            else:  # if another ship in the middle, delete the part of the ship
                   # alredy placed and return None
                for del_part in range(part):
                    board[bow[1]-ship_direction[1]*del_part]\
                         [bow[0]-ship_direction[0]*del_part] = None
                return
        return index

    

def fire(board,target):
    """implement a fire in battleship game

    Calling this function will try to destroy a part in one of the ships on the
    board. In case of successful fire destroy the relevant part
    in the damaged ship by deleting it from the board. deal also with the case
    of a ship which was completely destroyed

    -board - battleshipe board - you can assume its legal
    -target: a tuple of ints (x,y) indices on the board
    in case of illegal target return None

    returns: a tuple (hit,ship), where hit is True/False depending if the the
    shot hit, and ship is the index of the ship which was completely
    destroyed, or 0 if no ship was completely destroyed. or 0 if no ship
    was completely destroyed.

    Return None in case of bad input

    You can assume the board is legal. You can assume the other inputs
    are of the right form. You need to check that they are legal."""

    # verifies the input 
    if target[0] < 0 or target[0] > len(board[0]) - 1 or \
       target[1] < 0 or target[1] > len(board) - 1:
        return
    
    if board[target[1]][target[0]] is None: # when miss
        return False, 0
    else: # when hit
        destroyed_index = 0 # 0 if the ship didn't destroy completely
        # reduce the size of the ship
        board[target[1]][target[0]][2][0] = board[target[1]][target[0]][2][0] \
                                            - 1
        # check if the ship have been destroyed completely
        if board[target[1]][target[0]][2][0] == 0:
            # recieve the index of the destroyed ship
            destroyed_index = board[target[1]][target[0]][0]  
        board[target[1]][target[0]] = None  # remove the ship part from board
    return True, destroyed_index

    
    
