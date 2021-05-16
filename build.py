import os
from termcolor import colored

def build(to_include, directory='.', settings = {'flags': '', 'compiler': 'gcc'}):
    prev_directory = os.getcwd()
    if directory != '.':
        os.chdir(directory)
    cmd = settings['compiler'] + ' ' 
    for file in to_include:
        cmd += file + ' '
    cmd += ' -o ' + settings['app_name'] + ' ' + settings['flags']
    rc = os.WEXITSTATUS(os.system(cmd))
    os.chdir(prev_directory)
    if not rc:
        print(colored("Build successful", "green"))
    else:
        print(colored("Build failed", "red"))
    print()
    return rc