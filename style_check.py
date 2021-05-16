import os
from termcolor import colored

def check(files, directory='.'):
    print(colored('Style check:', 'blue'))
    for file in files:
        cmd = './CodeChecker.exe --rules "' + os.getcwd() + '/Rules.txt" "' + directory + file + '"'
        os.system(cmd)