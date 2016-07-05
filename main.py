# Main.py -  main function of this project, all functions to be defined here.
class DisjointSet:
    def __init__(self):
        self.Arr = []
        self.Size = []

    def initialize(self):
        for i in range(169):
            self.Arr.append(i)
            self.Size.append(1)

        for i in range(1, 12):
            self.Arr[i], self.Arr[156 + i] = 1, 156  # Top and Bottom virtual cells.
            self.Arr[13 * i], self.Arr[13 * i + 12] = 13, 25  # Left and Right virtual cells.

    def calc_id(self, x, y):
        return x * 13 + y

    def root(self, i):
        if self.Arr[i] != i:
            self.Arr[i] = self.root(self.Arr[i])
        return self.Arr[i]

    def merge(self, a, b):
        root_a, root_b = self.root(a), self.root(b)
        if root_a in [1, 156, 13, 25]:
            self.Arr[root_b], self.Size[root_a] = self.Arr[root_a], self.Size[root_a] + self.Size[root_b]
        elif root_b in [1, 156, 13, 25]:
            self.Arr[root_a], self.Size[root_b] = self.Arr[root_b], self.Size[root_b] + self.Size[root_a]
        elif root_a != root_b:
            if self.Size[root_a] < self.Size[root_b]:
                self.Arr[root_a], self.Size[root_b] = self.Arr[root_b], self.Size[root_b] + self.Size[root_a]
            else:
                self.Arr[root_b], self.Size[root_a] = self.Arr[root_a], self.Size[root_a] + self.Size[root_b]

    def find_set(self, a, b):
        return self.root(a) == self.root(b)


ds = DisjointSet()
ds.initialize()

# Board (13 * 13 matrix) initialized with 'U' --13x13 for virtual nodes
board = [['U' for j in range(13)] for i in range(13)]


# Function to fill in values for board
def initialize_board():
    for i in range(1, 12):
        board[i][0] = 'R'
        board[i][12] = 'R'
    board[0][1:12] = ['B'] * 11
    board[12][1:12] = ['B'] * 11
    board[0][0] = board[0][12] = board[12][0] = board[12][12] = 'O'  # virtual corners not required


initialize_board()


# TODO: function to print current status of board       --remove it
def print_board():
    spc = 0
    for i in board:
        print spc * ' ',
        for j in i:
            print j,
        spc += 1
        print


# This function checks whether a new piece can be placed or not.
def is_valid_move(r, c):
    if 0 <= r < 11 and 0 <= c < 11 and board[r + 1][c + 1] == 'U':
        return True
    else:
        return False


rvals = [0, 1, 0, -1, -1, 1]
cvals = [-1, -1, 1, 1, 0, 0]


def check_in_range(x, y):
    if x < 0 or x > 12 or y < 0 or y > 12:
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
# TODO: check_winning()
def check_winning():
    if ds.find_set(1, 156):
        return 'B'
    elif ds.find_set(13, 25):
        return 'R'
    return 'N'


# function to print current status of ds.Arr
def print_arr():
    for i in range(13):
        for j in range(13):
            print (str(ds.Arr[i * 13 + j]).zfill(3) + ' ' + str(i).zfill(2) + ' ' + str(j).zfill(2) + ' ' + str(
                board[i][j]) + '  '),
        print


def print_root():
    c = 0
    for i in range(169):
        if c == 13:
            c = 0
            print
        print str(ds.root(i)).zfill(3),
        c += 1


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
print check_winning()
