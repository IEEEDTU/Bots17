import os
import sys

codes = {200:'success',404:'file not found',400:'error',408:'timeout'}

def writeBoard(board):
    file = open('in.txt', 'w')
    for i in range(len(board)):
        for j in range(len(board[i])):
            file.write(str(board[i][j]))
            file.write(' ')
        file.write('\n')
    file.close()

def compileWindows(file, lang):
    if lang == 1:  # C
        class_file = file[:-2] + ".exe"
    elif lang == 2:  # C++
        class_file = file[:-4] + ".exe"
    elif lang == 3:  # Java
        class_file = file[:-4] + "class"
    else:  # No need to compile for Python
        return

    if (os.path.isfile(class_file)):
        os.remove(class_file)
        
    if (os.path.isfile(file)):
        if lang == 1:  # C 
            os.system('gcc -o ' + class_file + ' ' + file)
        elif lang == 2:  # C++
            os.system('g++ -o ' + class_file + ' ' + file)
        elif lang == 3:  # Java
            os.system('javac '+file)

        if (os.path.isfile(class_file)):
            return 200
        else:
            return 400
    else:
        return 404

def compileUnix(file, lang):
    if lang == 1:  # C
        class_file = file[:-2]
    elif lang == 2:  # C++
        class_file = file[:-4]
    elif lang == 3:  # Java
        class_file = file[:-4] + "class"
    else:  # No need to compile for Python
        return

    if (os.path.isfile(class_file)):
        os.remove(class_file)
        
    if (os.path.isfile(file)):
        if lang == 1:  # C 
            os.system('gcc -o ' + class_file + ' ' + file)
        elif lang == 2:  # C++
            os.system('g++ -o ' + class_file + ' ' + file)
        elif lang == 3:  # Java
            os.system('javac ' + file)

        if (os.path.isfile(class_file)):
            return 200
        else:
            return 400
    else:
        return 404

def runWindows(file, lang):
    if lang == 1:
        cmd = '.\\' + file[:-2]
    elif lang == 2:
        cmd = '.\\' + file[:-4]
    elif lang == 3:
        cmd = 'java ' + file[:-5]

    if 1 <= lang <= 3:
        r = os.system(cmd + ' < in.txt > out.txt')

    if 4 <= lang <= 5:
        r = os.system('python ' + file + ' < in.txt > out.txt')
        if r != 0:
            r = os.system('python3 ' + file + ' < in.txt > out.txt')
        if r != 0:
            r = os.system('py ' + file + ' < in.txt > out.txt')

    if lang == 1:  # C
        class_file = file[:-2] + ".exe"
    elif lang == 2:  # C++
        class_file = file[:-4] + ".exe"
    elif lang == 3:  # Java
        class_file = file[:-4] + "class"

    if (os.path.isfile(class_file)):
        os.remove(class_file)

    if r==0:
        return 200
    elif r==31744:
        os.remove('out.txt')
        return 408
    else:
        os.remove('out.txt')
        return 400

def runUnix(file, lang):
    if lang == 1:
        cmd = './' + file[:-2]
    elif lang == 2:
        cmd = './' + file[:-4]
    elif lang == 3:
        cmd = 'java ' + file[:-5]

    if 1 <= lang <= 3:
        r = os.system(cmd + ' < in.txt > out.txt')

    if 4 <= lang <= 5:
        r = os.system('python ' + file + ' < in.txt > out.txt')
        if r != 0:
            r = os.system('python3 ' + file + ' < in.txt > out.txt')
        if r != 0:
            r = os.system('py ' + file + ' < in.txt > out.txt')

    if lang == 1:  # C
        class_file = file[:-2]
    elif lang == 2:  # C++
        class_file = file[:-4]
    elif lang == 3:  # Java
        class_file = file[:-4] + "class"

    if (os.path.isfile(class_file)):
        os.remove(class_file)

    if r==0:
        return 200
    elif r==31744:
        os.remove('out.txt')
        return 408
    else:
        os.remove('out.txt')
        return 400

def readOutput():
    file.open('out.txt', 'r')
    x, y = file.read().split(' ')
    file.close()
    os.remove('in.txt')
    os.remove('out.txt')
    return x, y

def runCode(board, file, lang):
    writeBoard(board)
    if sys.platform == 'win32':
        compileWindows(file, lang)
        runWindows(file, lang)
    else:
        compileUnix(file, lang)
        runUnix(file, lang)
    return readOutput()