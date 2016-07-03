"""
Main file of the project. All functions are to be defined here.
"""

# Board (11 * 11 matrix) initialized with 'U'
board = [['U' for i in range(0, 11)] for j in range(0, 11)]

# This function checks whether a new piece can be placed or not.
def is_valid_move( x, y ):
	if(x<11 and y<11 and board[x][y]=='U'):
		return True;
	else:
		return False;

# This functions first checks for validity of new move and then
# update Board with new move.
def move(x, y, color):
	if(is_valid_move(x,y)):
		global board
		board[x][y] = color
		return True;
	else:
		return False;

# This function checks if any player is winning or not.
# TODO: check_winning()

# This function drives the program and plays the game.
# TODO: main function()

