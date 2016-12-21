import checker

def move(board, lang):
    file = {
        1: 'player1/play.c'
        2: 'player1/play.cpp'
        3: 'player1/play.java'
        4: 'player1/play_py2.py'
        5: 'player1/play_py3.py'
    }
    return checker.runCode(board, file[lang], lang)