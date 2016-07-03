"""
Main file of the project. All functions are to be defined here.
"""

# Board (11 * 11 matrix) initialized with 'U'
board = [['U' for i in range(0, 11)] for j in range(0, 11)]

#BoardHelp for Disjoint Set Matrix
boardHelp = [[0 for i in range(0,13)] for j in range (0,13)]
boardHelp[0][0] = -1 #Left hand top corner
boardHelp[0][12] = -2 #Right hand top corner
boardHelp[12][0] = -3 #Left hand bottom corner
boardHelp[12][12] = -4 #Right hand bottom corner
for i in range(1,12):
	boardHelp[i][0] = 1 #Virtual red column on left
	boardHelp[i][12] = 2 #Virtual red column on right
	boardHelp[0][i] = 3 #Virtual blue row on top
	boardHelp[12][i] = 4 #Virtual blue row on bottom

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
			boardHelp[x+1][y+1] = 1
			if(y==10):
				boardHelp[x+2][12] = 1
				
		else:
			global boardHelp
			boardHelp[x+1][y+1] = 3
			if(x==10):
				boardHelp[12][y+2] = 3
		
		if(check_winning(color)):
			print color  + "wins!"

		return True


	else:
		return False

# This function checks if any player is winning or not.
# TODO: check_winning()
def check_winning(color):
	if(color=='R'):
		for i in range(0,13):
			if(boardHelp[i][12]==1):
				return checkconnectedred(i-1,11,i,12)
		return False		

	else:
		for i in range(0,13):
			if(boardHelp[12][i]==3):
				return checkconnectedblue(11,i-1,12,i)
		return False

def checkconnectedred(x,y,xpar,ypar):
	retval = False
	if(y==1):
		return True

	if(x-1>0 and x-1<12 and retval==False and x-1!=xpar):
		if(boardHelp[x-1][y]==1):
			retval = checkconnectedred(x-1,y,x,y)
		else:
			retval = False
	
	if(x-1>0 and x-1<12 and y-1>0 and y-1<12 and retval==False and (x-1!=xpar or y-1!=ypar)):
		if(boardHelp[x-1][y-1]==1):
			retval = checkconnectedred(x-1,y-1,x,y)
		else:
			retval = False
		
	
	if(x-1>0 and x-1<12 and y+1>0 and y+1<12 and retval==False and (x-1!=xpar or y+1!=ypar)):
		if(boardHelp[x-1][y+1]==1):
			retval = checkconnectedred(x-1,y+1,x,y)
		else:
			retval = False
		 

	if(x+1>0 and x+1<12 and retval==False and x+1!=xpar):
		if(boardHelp[x+1][y]==1):
			retval = checkconnectedred(x+1,y,x,y)
		else:
			retval = False
		 
	
	if(x+1>0 and x+1<12 and y-1>0 and y-1<12 and retval==False and (x+1!=xpar or y-1!=ypar)):
		if(boardHelp[x+1][y-1]==1):
			retval = checkconnectedred(x+1,y-1,x,y)
		else:
			retval = False
		 
	
	if(x+1>0 and x+1<12 and y+1>0 and y+1<12 and retval==False and (x+1!=xpar or y+1!=ypar)):
		if(boardHelp[x+1][y+1]==1):
			retval = checkconnectedred(x+1,y+1,x,y)	
		else:
			retval = False
		 

	if(y-1>0 and y-1<12 and retval==False and ypar!=y-1):
		if(boardHelp[x][y-1]==1):
			retval = checkconnectedred(x,y-1,x,y)
		else:
			retval = False
		 

	if(y+1>0 and y+1<12 and ypar!=y+1 and retval==False):
		if(boardHelp[x][y+1]==1):
			retval = checkconnectedred(x,y+1,x,y)
		else:
			retval = False
		 

	return retval

def checkconnectedblue(x,y,xpar,ypar):
	retval = False
	if(y==1):
		return True

	if(x-1>0 and x-1<12 and retval==False and x-1!=xpar):
		if(boardHelp[x-1][y]==3):
			retval = checkconnectedred(x-1,y,x,y)
		else:
			retval = False
	
	if(x-1>0 and x-1<12 and y-1>0 and y-1<12 and retval==False and (x-1!=xpar or y-1!=ypar)):
		if(boardHelp[x-1][y-1]==3):
			retval = checkconnectedred(x-1,y-1,x,y)
		else:
			retval = False
		
	
	if(x-1>0 and x-1<12 and y+1>0 and y+1<12 and retval==False and (x-1!=xpar or y+1!=ypar)):
		if(boardHelp[x-1][y+1]==3):
			retval = checkconnectedred(x-1,y+1,x,y)
		else:
			retval = False
		 

	if(x+1>0 and x+1<12 and retval==False and x+1!=xpar):
		if(boardHelp[x+1][y]==3):
			retval = checkconnectedred(x+1,y,x,y)
		else:
			retval = False
		 
	
	if(x+1>0 and x+1<12 and y-1>0 and y-1<12 and retval==False and (x+1!=xpar or y-1!=ypar)):
		if(boardHelp[x+1][y-1]==3):
			retval = checkconnectedred(x+1,y-1,x,y)
		else:
			retval = False
		 
	
	if(x+1>0 and x+1<12 and y+1>0 and y+1<12 and retval==False and (x+1!=xpar or y+1!=ypar)):
		if(boardHelp[x+1][y+1]==3):
			retval = checkconnectedred(x+1,y+1,x,y)	
		else:
			retval = False
		 

	if(y-1>0 and y-1<12 and retval==False and ypar!=y-1):
		if(boardHelp[x][y-1]==3):
			retval = checkconnectedred(x,y-1,x,y)
		else:
			retval = False
		 

	if(y+1>0 and y+1<12 and ypar!=y+1 and retval==False):
		if(boardHelp[x][y+1]==3):
			retval = checkconnectedred(x,y+1,x,y)
		else:
			retval = False
		 

	return retval

# This function drives the program and plays the game.
# TODO: main function()

