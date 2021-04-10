import build
import run_tests
import style_check
from pathlib import Path

ADDRESS_STYLE = 'PARENT' # 'PARENT' / 'CURRENT' / 'ABSOLUTE'

directory = ''

if ADDRESS_STYLE == 'PARENT':
    folder = input('Input folder name: ')
    if folder != '':
        folder = '/' + folder + '/'
    path = Path(__file__).resolve().parents[1].as_posix()
    directory = path + folder
elif ADDRESS_STYLE == 'CURRENT':
    folder = input('Input folder name: ')
    if folder != '':
        folder = '/' + folder + '/'
    path = Path(__file__).resolve().parents[0].as_posix()
    directory = path + folder
elif ADDRESS_STYLE == 'ABSOLUTE':
    directory = input('Input folder\'s absolute path: ')
    if directory[-1] != '/':
        directory += '/'

if directory != '':
    build.build('main.c', 'app', directory=directory)
    run_tests.run('main.c', 'app', directory=directory)
    style_check.check('main.c', directory=directory)