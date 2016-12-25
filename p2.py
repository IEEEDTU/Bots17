import checker

file = {
    1: 'player2/play.c',
    2: 'player2/play.cpp',
    3: 'player2/Play.java',
    4: 'player2/play_py2.py',
    5: 'player2/play_py3.py',
}

def move(board, lang, isFirstMove):
    return checker.runCode(board, 'B', file[lang], lang, isFirstMove)

def delete_classfiles(lang):
    checker.delete_classfiles(file[lang], lang)