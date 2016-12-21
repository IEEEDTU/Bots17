import checker

def move(board, lang):
    file = {
        1: 'player2/play.c'
        2: 'player2/play.cpp'
        3: 'player2/play.java'
        4: 'player2/play_py2.py'
        5: 'player2/play_py3.py'
    }
    return checker.runCode(board, file[lang], lang)