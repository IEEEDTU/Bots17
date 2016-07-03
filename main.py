"""
Main file of the project. All functions are to be defined here.
"""

# Board (11 * 11 matrix) initialized with 'U'
board = [['U' for i in range(0, 11)] for j in range(0, 11)]

#BoardHelp for Disjoint Set Matrix
#0 for 'U', 1 for 'R', 2 for 'B'
boardHelp = [[0 for i in range(0,11)] for j in range (0,11)]

# This function checks whether a new piece can be placed or not.
def is_valid_move( x, y ):
	if 0 <= x < 11 and 0 <= y < 11 and board[x][y] == 'U':
		return True
	else:
		return False

# This functions first checks for validity of new move and then
# update Board with new move.
def move(x, y, color):
	if(is_valid_move(x,y)):
		global board
		board[x][y] = color
		if(color=='R'):
			global boardHelp
			boardHelp[x][y] = 1
			
		else:
			global boardHelp
			boardHelp[x][y] = 2
			
		if(check_winning(color)):
			print color  + "wins!"

		return True


	else:
		return False

# This function checks if any player is winning or not.
# TODO: check_winning()
def check_winning(color):
	if(color=='R'):
		for i in range(0,11):
			if(boardHelp[i][10]==1):
				return check_connected(i,10,i,10,1)
		return False		

	else:
		for i in range(0,11):
			if(boardHelp[10][i]==2):
				return check_connected(10,i,10,i,2)
		return False

def check_connected(x,y,xpar,ypar,col):
	retval = False
	print x, y
	if(y==1):
		return True

	if(x-1>=0 and x-1<11 and retval==False and x-1!=xpar):
		if(boardHelp[x-1][y]==col):
			retval = check_connected(x-1,y,x,y,col)
		else:
			retval = False
	
	if(x-1>=0 and x-1<11 and y-1>=0 and y-1<11 and retval==False and (x-1!=xpar or y-1!=ypar)):
		if(boardHelp[x-1][y-1]==col):
			retval = check_connected(x-1,y-1,x,y,col)
		else:
			retval = False
		
	
	if(x-1>=0 and x-1<11 and y+1>=0 and y+1<11 and retval==False and (x-1!=xpar or y+1!=ypar)):
		if(boardHelp[x-1][y+1]==col):
			retval = check_connected(x-1,y+1,x,y,col)
		else:
			retval = False
		 

	if(x+1>=0 and x+1<11 and retval==False and x+1!=xpar):
		if(boardHelp[x+1][y]==col):
			retval = check_connected(x+1,y,x,y,col)
		else:
			retval = False
		 
	
	if(x+1>=0 and x+1<11 and y-1>=0 and y-1<11 and retval==False and (x+1!=xpar or y-1!=ypar)):
		if(boardHelp[x+1][y-1]==col):
			retval = check_connected(x+1,y-1,x,y,col)
		else:
			retval = False
		 
	
	if(x+1>=0 and x+1<11 and y+1>=0 and y+1<11 and retval==False and (x+1!=xpar or y+1!=ypar)):
		if(boardHelp[x+1][y+1]==col):
			retval = check_connected(x+1,y+1,x,y,col)	
		else:
			retval = False
		 

	if(y-1>=0 and y-1<11 and retval==False and ypar!=y-1):
		if(boardHelp[x][y-1]==col):
			retval = check_connected(x,y-1,x,y,col)
		else:
			retval = False
		 

	if(y+1>=0 and y+1<11 and ypar!=y+1 and retval==False):
		if(boardHelp[x][y+1]==col):
			retval = check_connected(x,y+1,x,y,col)
		else:
			retval = False
		 

	return retval

# This function drives the program and plays the game.
# TODO: main function()

