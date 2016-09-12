import timeit
from main import move


def func():
    for i in range(11):
        for j in range(11 - i - 1):
            move(i, j, 'R')

    for i in range(1, 11):
        for j in range(i):
            move(i, 11 - j - 1, 'B')

    move(10, 0, 'R')
    move(0, 10, 'B')


func()
