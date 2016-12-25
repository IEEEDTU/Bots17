import checker

file = {
    1: 'player1/play.c',
    2: 'player1/play.cpp',
    3: 'player1/Play.java',
    4: 'player1/play_py2.py',
    5: 'player1/play_py3.py',
}

def move(board, lang, isFirstMove):
    return checker.runCode(board, file[lang], lang, isFirstMove)

def delete_classfiles(lang):
    checker.delete_classfiles(file[lang], lang)