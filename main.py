"""
Main file of the project. All functions are to be defined here.
"""

from disjointset import DisjointSet

ds = DisjointSet()
ds.initialize()

# Board (11 * 11 matrix) initialized with 'U'
board = [['U' for j in range(11)] for i in range(11)]

# BoardHelp for Disjoint Set Matrix
# 0 for 'U', 1 for 'R', 2 for 'B'
boardHelp = [[0 for i in range(0, 11)] for j in range(0, 11)]


# This function checks whether a new piece can be placed or not.
def is_valid_move(r, c):
    if 0 <= r < 11 and 0 <= c < 11 and board[r][c] == 'U':
        return True
    else:
        return False


rvals = [0, 1, 0, -1, -1, 1]
cvals = [-1, -1, 1, 1, 0, 0]


def check_in_range(x, y):
    if x < 0 or x > 10 or y < 0 or y > 10:
        return False
    return True


def get_connected_components(x, y):
    global board
    retval, color = [], board[x][y]
    for k in range(6):
        a, b = x + cvals[k], y + rvals[k]
        if check_in_range(a, b):
            if board[a][b] == color:
                retval.append((a, b))
    return retval


# This functions first checks for validity of new move and then
# update Board with new move.
<<<<<<< HEAD
def move(r, c, color):
    global board
    if is_valid_move(r, c):
        board[r][c] = color
        conn_comps = get_connected_components(r, c)
        print color, conn_comps
        spc = 0
        for i in board:
            print spc*' ',
            for j in i:
                print j,
            spc += 1
            print
        id0 = ds.calc_id(r, c)
        for cell in conn_comps:
            x, y = cell
            id1 = ds.calc_id(x, y)
            ds.merge(id0, id1)
=======
def move(x, y, color):
    if is_valid_move(x, y):
        global board, boardHelp
        board[x][y] = color
        if color == 'R':
            boardHelp[x][y] = 1
        else:
            boardHelp[x][y] = 2

        if check_winning(color):
            print(color + " wins!")

>>>>>>> origin/master
        return True
    else:
        return False


# This function checks if any player is winning or not.
# TODO: check_winning()
def check_winning(color):
    if color == 'R':
        for i in range(0, 11):
            if boardHelp[i][10] == 1:
                return check_connected(i, 10, i, 10, 1)
        return False

<<<<<<< HEAD
def check_winning():
    if ds.find_set(1, 117):
        return 'B'
    elif ds.find_set(13, 25):
        return 'R'
    return 'N'


# This function drives the program and plays the game.
# TODO: main function()

move(5, 5, 'R')
move(9, 1, 'B')
move(6, 3, 'R')
move(8, 1, 'B')
move(7, 1, 'R')
move(7, 2, 'B')
move(6, 2, 'R')
move(7, 0, 'B')
move(8, 0, 'R')
move(6, 1, 'B')
move(4, 7, 'R')
move(5, 2, 'B')
move(4, 8, 'R')
move(4, 3, 'B')
move(10, 3, 'R')
move(3, 4, 'B')
move(6, 4, 'R')
move(2, 5, 'B')
move(5, 6, 'R')
move(1, 6, 'B')
move(10, 0, 'R')
move(0, 7, 'B')
move(10, 4, 'R')
move(10, 1, 'B')
move(5, 8, 'R')
move(4, 9, 'B')
move(10, 2, 'R')
move(3, 9, 'B')
move(5, 9, 'R')
move(2, 9, 'B')
move(5, 10, 'R')
=======
    else:
        for i in range(0, 11):
            if boardHelp[10][i] == 2:
                return check_connected(10, i, 10, i, 2)
        return False


def check_connected(x, y, xpar, ypar, col):
    retval = False
    if col == 1 and y == 0:
        return True
    if col == 2 and x == 0:
        return True

    if 0 <= x - 1 < 11 and retval is False and x - 1 != xpar:
        if boardHelp[x - 1][y] == col:
            retval = check_connected(x - 1, y, x, y, col)
        else:
            retval = False

    if 0 <= x - 1 < 11 and 0 <= y + 1 < 11 and retval is False and (x - 1 != xpar or y + 1 != ypar):
        if boardHelp[x - 1][y + 1] == col:
            retval = check_connected(x - 1, y + 1, x, y, col)
        else:
            retval = False

    if 0 <= x + 1 < 11 and retval is False and x + 1 != xpar:
        if boardHelp[x + 1][y] == col:
            retval = check_connected(x + 1, y, x, y, col)
        else:
            retval = False

    if 0 <= x + 1 < 11 and 0 <= y - 1 < 11 and retval is False and (x + 1 != xpar or y - 1 != ypar):
        if boardHelp[x + 1][y - 1] == col:
            retval = check_connected(x + 1, y - 1, x, y, col)
        else:
            retval = False

    if 0 <= y - 1 < 11 and retval == False and ypar != y - 1:
        if boardHelp[x][y - 1] == col:
            retval = check_connected(x, y - 1, x, y, col)
        else:
            retval = False

    if 0 <= y + 1 < 11 and ypar != y + 1 and retval == False:
        if boardHelp[x][y + 1] == col:
            retval = check_connected(x, y + 1, x, y, col)
        else:
            retval = False

    return retval

# This function drives the program and plays the game.
# TODO: main function()
>>>>>>> origin/master
