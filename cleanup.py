import os

def cleanup(directory = '.', settings = {}):
    prevdir = os.getcwd()
    if directory != '.':
        os.chdir(directory)
    cmd = 'rm -f "' + settings['app_name'] + '" tmp.txt *.gcov *.gcda *.gcno'
    os.system(cmd)
    os.chdir(prevdir)