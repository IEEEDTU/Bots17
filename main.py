import p1, p2
import disjoint

# Main.py -  main function of this project, all functions to be defined here.
ds = disjoint.DisjointSet()
ds.initialize()

# Board (13 * 13 matrix) initialized with 'U' --13x13 for virtual nodes
board = [['U' for j in range(13)] for i in range(13)]

# Connected cells
rvals = [0, 1, 0, -1, -1, 1]
cvals = [-1, -1, 1, 1, 0, 0]

# Function to fill in values for board
def initialize_board():
    global board
    for i in range(1, 12):
        board[i][0] = 'R'
        board[i][12] = 'R'
    board[0][1:12] = ['B'] * 11
    board[12][0:11] = ['B'] * 11
    board[0][0] = board[0][12] = board[12][0] = board[12][12] = 'O'  # virtual corners not required

# This function checks whether a cell in board is occupied or empty
is_cell_empty = lambda r, c : board[r+1][c+1] == 'U'

# This function checks whether a new piece can be placed or not.
is_valid_move = lambda r, c : 0 <= r < 11 and 0 <= c < 11 and board[r + 1][c + 1] == 'U'

# This function checks whether a cell is inside board or not
check_in_range = lambda x, y : 0 <= x < 13 and 0 <= y < 13

# This function returns a list of Connected cells with same color stone
def get_connected_components(x, y):
    global board, rvals, cvals
    ret, color = [], board[x][y]
    for k in range(6):
        a, b = x + cvals[k], y + rvals[k]
        if check_in_range(a, b):
            if board[a][b] == color:
                ret.append((a, b))
    return ret

# This functions first checks for validity of new move and then update Board with new move.
def move(r, c, color):
    global board
    if is_valid_move(r, c):
        r, c = r + 1, c + 1
        board[r][c] = color
        conn_comps = get_connected_components(r, c)
        id0 = ds.calc_id(r, c)
        for cell in conn_comps:
            x, y = cell
            id1 = ds.calc_id(x, y)
            ds.merge(id0, id1)

# This function checks if any player is winning or not.
def check_winning():
    if ds.find_set(1, 156):
        return 'B'
    elif ds.find_set(13, 25):
        return 'R'
    return None

get_player = lambda color : {'R':'P1', 'B':'P2'}[color]

get_other = lambda color : {'R':'P2', 'B':'P1'}[color]

# This function drives the program and plays the game.
def main():
    global board
    initialize_board()

    # P1's first turn.
    player, color, lang = p1, 'R', lang1
    x, y = player.move([i[1:-1] for i in board[1:-1]], lang, True)  # For giving 11X11 matrix
    if (x, y) == ('x', 'x'):
        print(get_other(color), "wins!")
        return
    x, y = int(x), int(y)
    if not is_valid_move(x, y):
        print("Invalid move")
        print(get_other(color), "wins!")
        return
    else:
        move(x, y, color)
        print(get_player(color), color, (x, y))

    # P2's first turn
    player, color, lang = p2, 'B', lang2
    x, y = player.move([i[1:-1] for i in board[1:-1]], lang, True)  # For giving 11X11 matrix
    if (x, y) == ('x', 'x'):
        print(get_other(color), "wins!")
        return
    x, y = int(x), int(y)
    if not 0 <= x < 11 or not 0 <= y < 11:
        print("Invalid move")
        print(get_other(color), "wins!")
        return

    if is_cell_empty(x, y):
        move(x, y, color)
        print(get_player(color), color, (x, y))
    else:  # player 2 will return coordinates of red stone to swap i.e. board[x][y] == 'R'
        board[x][y] = 'U'
        move(x, y, color)
        print(get_player(color), color, (x, y), 'Swap!')

    # Normal gameplay
    while not check_winning():
        player, color, lang = (p2, 'B', lang2) if (player == p1) else (p1, 'R', lang1)
        x, y = player.move([i[1:-1] for i in board[1:-1]], lang, False)  # For giving 11X11 matrix
        if (x, y) == ('x', 'x'):
            print(get_other(color), "wins!")
            return
        x, y = int(x), int(y)
        if not is_valid_move(x, y):
            print("Invalid move")
            print(get_other(color), "wins!")
            return
        else:
            move(x, y, color)
            print(get_player(color), color, (x, y))

    # The game has ended. Declare the winner
    print(get_player(check_winning()), ' wins!')

# This is for selecting language.
langs = {
        1: "C",
        2: "C++",
        3: "Java",
        4: "Python2",
        5: "Python3",
}

def print_menu():
    for i in range(1, 6):
        print("%d."%(i), langs[i]) 

print_menu()
lang1 = int(input("Select language for player 1(1-5): "))
lang2 = int(input("Select language for player 2(1-5): "))

if 1 <= lang1 <= 5 and 1 <= lang2 <= 5:
    print("You have selected the following: ")
    print("P1:", langs[lang1])
    print("P2:", langs[lang2])
    main()
    p1.delete_classfiles(lang1)
    p2.delete_classfiles(lang2)
else:
    print("Invalid language selection.")
