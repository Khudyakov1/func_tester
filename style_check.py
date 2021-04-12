import os
from termcolor import colored

def check(app_name, directory='.'):
    print(colored('Style check:', 'blue'))
    cmd = './CodeChecker.exe --rules "' + os.getcwd() + '/Rules.txt" "' + directory + app_name + '"'
    os.system(cmd)