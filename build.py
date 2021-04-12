import os
from termcolor import colored

def build(file_name, app_name, directory='.', flags='-Wall -Werror -Wextra -Wpedantic -Wvla -Wfloat-equal -Wfloat-conversion --coverage -lm', compiler='gcc'):
    prev_directory = os.getcwd()
    if directory != '.':
        os.chdir(directory)
    cmd = compiler + ' ' + file_name + ' -o ' + app_name + ' ' + flags
    #os.system(cmd)
    rc = os.WEXITSTATUS(os.system(cmd))
    os.chdir(prev_directory)
    if not rc:
        print(colored("Build successful", "green"))
    else:
        print(colored("Build failed", "red"))
    print()
    return rc