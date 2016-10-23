# The participant needs to edit the below function with his own code.
# The function accepts 11x11 matrix as input, which represents rhombus hex game board.
# board[i][j]: 'U' -> Unoccupied or empty slot, 'R' -> Red stone, 'B' -> Blue stone.
# The function should return x, y as coordinates to place his new move.

bluemove = [(9, 1), (8, 1), (7, 2), (7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7), (10, 1), (4, 9), (3, 9), (2, 9)]
#bluemove = [('.','.')]+[(i,11-j-1) for i in range(1,11) for j in range(i)]+[(0, 10)]
indblue=0

import random
def move(board):
	global bluemove,indblue
	indblue+=1
	return bluemove[indblue-1]
