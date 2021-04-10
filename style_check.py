import os

def check(app_name, directory='.'):
    print("Style check:")
    cmd = './CodeChecker.exe --rules "' + os.getcwd() + '/Rules.txt" "' + directory + app_name + '"'
    os.system(cmd)