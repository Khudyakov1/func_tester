import build
import run_tests
import style_check
import find_file
import settings
import cleanup
from pathlib import Path
from termcolor import colored

ADDRESS_STYLE = 'PARENT' # 'PARENT' / 'CURRENT' / 'ABSOLUTE'
STRICT_STRING = True
DEFAULT_SETTINGS = {
    'strict_string': False,
    'result_word': '',
    'app_name': 'app.exe',
    'coverage': True,
    'style_check': True,
    'cleanup': True,
    'flags': '-Wall -Werror -Wextra -Wpedantic -Wvla -Wfloat-equal -Wfloat-conversion --coverage -lm',
    'compiler': 'gcc',
    'tests_folder': 'func_tests',
    'positive_test_mask': 'pos_*_*.txt',
    'negative_test_mask': 'neg_*_*.txt',

}

directory = ''

if ADDRESS_STYLE == 'PARENT':
    folder = input(colored('Input folder name: ', 'blue'))
    if folder != '':
        folder = '/' + folder + '/'
    path = Path(__file__).resolve().parents[1].as_posix()
    directory = path + folder
elif ADDRESS_STYLE == 'CURRENT':
    folder = input(colored('Input folder name: ', 'blue'))
    if folder != '':
        folder = '/' + folder + '/'
    path = Path(__file__).resolve().parents[0].as_posix()
    directory = path + folder
elif ADDRESS_STYLE == 'ABSOLUTE':
    directory = input(colored('Input folder\'s absolute path: ', 'blue'))
    if directory[-1] != '/':
        directory += '/'

if directory != '':
    config = settings.open_settings(default_settings=DEFAULT_SETTINGS, directory=directory)
    files = find_file.find_files(directory=directory)
    if not build.build(files, directory=directory, settings=config):
        run_tests.run(directory=directory, settings=config)
        if config['style_check']:
            style_check.check(files, directory=directory)
        if config['cleanup']:
            cleanup.cleanup(directory=directory, settings=config)