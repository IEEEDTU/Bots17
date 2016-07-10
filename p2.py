# The participant needs to edit the below function with his own code.
# The function accepts 11x11 matrix as input, which represents rhombus hex game board.
# board[i][j]: 'U' -> Unoccupied or empty slot, 'R' -> Red stone, 'B' -> Blue stone.
# The function should return x, y as coordinates to place his new move.

import random
def move(board):
    x,y = random.randint(0,10),random.randint(0,10)
    while board[x][y] !='U':
        x,y = random.randint(0,10),random.randint(0,10)
    return x,y
