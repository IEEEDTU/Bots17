import os
import sys
import subprocess
import time

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
        cmd = '.\\' + file[:7] + '\\' + file[8:-2]
    elif lang == 2:
        cmd = '.\\' + file[:7] + '\\' + file[8:-4]
    elif lang == 3:
        cmd = 'java -cp ' + file[:8] + ' ' + file[8:-5]

    if 1 <= lang <= 3:
        r = os.system(cmd + ' < in.txt > out.txt')

    FNULL = open(os.devnull, 'w')
    if 4 <= lang <= 5:
        r = subprocess.call('python ' + file + ' < in.txt > out.txt', shell=True, stdout=FNULL, stderr=FNULL)
        if r != 0:
            r = subprocess.call('python3 ' + file + ' < in.txt > out.txt', shell=True, stdout=FNULL, stderr=FNULL)
        if r != 0:
            r = subprocess.call('py ' + file + ' < in.txt > out.txt', shell=True, stdout=FNULL, stderr=FNULL)

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
        cmd = 'java -cp ' + file[:8] + ' ' + file[8:-5]

    if 1 <= lang <= 3:
        r = os.system(cmd + ' < in.txt > out.txt')

    FNULL = open(os.devnull, 'w')
    if 4 <= lang <= 5:
        r = subprocess.call('python ' + file + ' < in.txt > out.txt', shell=True, stdout=FNULL, stderr=FNULL)
        if r != 0:
            r = subprocess.call('python3 ' + file + ' < in.txt > out.txt', shell=True, stdout=FNULL, stderr=FNULL)
        if r != 0:
            r = subprocess.call('py ' + file + ' < in.txt > out.txt', shell=True, stdout=FNULL, stderr=FNULL)

    if r==0:
        return 200
    elif r==31744:
        os.remove('out.txt')
        return 408
    else:
        os.remove('out.txt')
        return 400

def readOutput():
    file = open('out.txt', 'r')
    x, y = file.read().split(' ')
    file.close()
    delete_temp()
    return x, y

def delete_temp():
    if os.path.isfile('in.txt'):
        os.remove('in.txt')
    if os.path.isfile('out.txt'):
        os.remove('out.txt')

def delete_classfiles(file, lang):
    class_file = ""
    if sys.platform == 'win32':
        if lang == 1:  # C
            class_file = file[:-2] + ".exe"
        elif lang == 2:  # C++
            class_file = file[:-4] + ".exe"
        elif lang == 3:  # Java
            class_file = file[:-4] + "class"
    else:   
        if lang == 1:  # C
            class_file = file[:-2]
        elif lang == 2:  # C++
            class_file = file[:-4]
        elif lang == 3:  # Java
            class_file = file[:-4] + "class"

    if (os.path.isfile(class_file)):
        os.remove(class_file)


def runCode(board, file, lang, isFirstMove):
    writeBoard(board)

    if isFirstMove:
        r = compileWindows(file, lang) if sys.platform == 'win32' else compileWindows(file, lang)
        if r == 400:
            print('Compilation Failed: Compilation Error')
            delete_temp()
            return 'x', 'x'
        elif r == 404:
            print('Compilation Failed: File Not Found')
            delete_temp()
            return 'x', 'x'

    start = time.time()
    r = runWindows(file, lang) if sys.platform == 'win32' else runWindows(file, lang)
    t = time.time() - start

    if r == 400:
        print('Execution Failed: Runtime Error')
        delete_temp()
        return 'x', 'x'
    elif r == 404:
        print('Execution Failed: File Not Found')
        delete_temp()
        return 'x', 'x'
    elif t > 5 and 1 <= lang <= 2:
        print('Time Limit Exceeded')
        delete_temp()
        return 'x', 'x'
    elif t > 10 and lang == 3:
        print('Time Limit Exceeded')
        delete_temp()
        return 'x', 'x'
    elif t > 15 and 4 <= lang <= 5:
        print('Time Limit Exceeded')
        delete_temp()
        return 'x', 'x'
    
    x, y = readOutput()
    if not x[:1].isdigit() or not y[:1].isdigit():
        print('Invalid output')
        return 'x', 'x'
    else:
        return x, y