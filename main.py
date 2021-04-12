import build
import run_tests
import style_check
from pathlib import Path
from termcolor import colored

ADDRESS_STYLE = 'PARENT' # 'PARENT' / 'CURRENT' / 'ABSOLUTE'

directory = ''

if ADDRESS_STYLE == 'PARENT':
    folder = input(colored('Input folder name: ', 'blue'))
    if folder != '':
        folder = '/' + folder + '/'
    path = Path(__file__).resolve().parents[1].as_posix()
    directory = path + folder
elif ADDRESS_STYLE == 'CURRENT':
    folder = nput(colored('Input folder name: ', 'blue'))
    if folder != '':
        folder = '/' + folder + '/'
    path = Path(__file__).resolve().parents[0].as_posix()
    directory = path + folder
elif ADDRESS_STYLE == 'ABSOLUTE':
    directory = input(colored('Input folder\'s absolute path: ', 'blue'))
    if directory[-1] != '/':
        directory += '/'

if directory != '':
    if not build.build('main.c', 'app', directory=directory):
        run_tests.run('main.c', 'app', directory=directory)
        style_check.check('main.c', directory=directory)