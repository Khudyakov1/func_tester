import os
from termcolor import colored

def find_files(directory='.'):
    prev_directory = os.getcwd()
    if directory != '.':
        os.chdir(directory)
    to_include = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".c"):
                answer = ''
                while answer.lower() not in ['y', 'yes', 'no', 'n']:
                    answer = input('Include ' + colored(file, 'magenta') + '? (Y/n): ')
                if answer.lower() in ['y','yes']:
                    to_include.append(file)
    os.chdir(prev_directory)
    return to_include