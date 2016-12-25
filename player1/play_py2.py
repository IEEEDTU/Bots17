# Edit this function with your code.
def move(board):
     import random
     x, y = random.randrange(0, 11), random.randrange(0, 11)
     while board[x][y] != 'U':
         x, y = random.randrange(0, 11), random.randrange(0, 11)
     return x, y

board = [raw_input().split() for i in range(11)]
color = raw_input()
x, y = move(board)
print x, y