# The participant needs to edit the below function with his own code.
# The function accepts 11x11 matrix as input, which represents rhombus hex game board.
# board[i][j]: 'U' -> Unoccupied or empty slot, 'R' -> Red stone, 'B' -> Blue stone.
# The function should return x, y as coordinates to place his new move.

redmove = [(5, 5), (6, 3), (7, 1), (6, 2), (8, 0), (4, 7), (4, 8), (10, 3), (6, 4), (5, 6), (10, 0), (10, 4), (5, 8), (10, 2), (5, 9), (5, 10)]
#redmove = [(i,j) for i in range(11) for j in range(11-i-1)]+[(10, 0)]
indred = 0

def move(board):
	global redmove,indred
	indred+=1
	return redmove[indred-1]