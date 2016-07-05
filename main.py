"""
Main file of the project. All functions are to be defined here.
"""

# Board (11 * 11 matrix) initialized with 'U'
board = [['U' for i in range(0, 11)] for j in range(0, 11)]

#boardHelp for Disjoint Set Matrix
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
			print((color) + " wins!")

		return True


	else:
		return False

# This function checks if any player is winning or not.
# TODO: check_winning()
def check_winning(color):
#Check if atleast one red cell in all columns
	if(color=='R'):
		for a in range(0,11):
			if(boardHelp[a][10]==1):
				for b in range(0,11):
					if(boardHelp[b][9]==1):
						for c in range(0,11):
							if(boardHelp[c][8]==1):
								for d in range(0,11):
									if(boardHelp[d][7]==1):
										for e in range(0,11):
											if(boardHelp[e][6]==1):
												for f in range(0,11):
													if(boardHelp[f][5]==1):
														for g in range(0,11):
															if(boardHelp[g][4]==1):
																for h in range(0,11):
																	if(boardHelp[h][3]==1):
																		for i in range(0,11):
																			if(boardHelp[i][2]==1):
																				for j in range(0,11):
																					if(boardHelp[j][1]==1):
																						for k in range(0,11):
																							if(boardHelp[k][0]==1):
																								return check_connected(i,10,i,10,1)						
		return False		
#Check if atleast one blue cell in all rows
	else:
		for a in range(0,11):
			if(boardHelp[10][a]==1):
				for b in range(0,11):
					if(boardHelp[9][b]==1):
						for c in range(0,11):
							if(boardHelp[8][c]==1):
								for d in range(0,11):
									if(boardHelp[7][d]==1):
										for e in range(0,11):
											if(boardHelp[6][e]==1):
												for f in range(0,11):
													if(boardHelp[5][f]==1):
														for g in range(0,11):
															if(boardHelp[4][g]==1):
																for h in range(0,11):
																	if(boardHelp[3][h]==1):
																		for i in range(0,11):
																			if(boardHelp[2][i]==1):
																				for j in range(0,11):
																					if(boardHelp[1][j]==1):
																						for k in range(0,11):
																							if(boardHelp[0][k]==1):
																								return check_connected(10,i,10,i,2)
			return False

def check_connected(x,y,xpar,ypar,col):		
	retval = False
	if(col==1 and y==0):
		return True
	if(col==2 and x==0):
		return True

	if(x-1>=0 and x-1<11 and retval==False and x-1!=xpar):
		if(boardHelp[x-1][y]==col):
			retval = check_connected(x-1,y,x,y,col)
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

def main_func():
	for i in range(11):
		for j in range(11 - i - 1):
			move(i, j, 'R')

	for i in range(1, 11):
		for j in range(i):
			move(i, 11 - j - 1, 'B')

	move(0, 10, 'R')

