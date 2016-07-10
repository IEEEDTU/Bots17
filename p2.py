# The participant needs to edit the below function with his own code.
# The function accepts 11x11 matrix as input, which represents rhombus hex game board.
# board[i][j]: 'U' -> Unoccupied or empty slot, 'R' -> Red stone, 'B' -> Blue stone.
# The function should return x, y as coordinates to place his new move.


def move(board):
    import random
    x, y = random.randrange(1, 11), random.randrange(1, 11)
    while board[x][y] != 'U':
        x, y = random.randrange(1, 11), random.randrange(1, 11)
    return x, y
