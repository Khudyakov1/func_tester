import os
from termcolor import colored

def leave_numbers(string):
    numbers = ['0','1','2','3','4','5','6','7','8','9','-',' ']
    result = ''
    for k in string:
        if k in numbers or k == '.':
            result += k
    while result.find('  ') != -1:
        result = result.replace('  ',' ')
    result = result.strip()
    return result

def run(directory='.', settings = {}):
    tests_passed = True
    prev_directory = os.getcwd()
    if directory != '.':
        os.chdir(directory)
    directory = os.getcwd()
    cmd = 'rm "' + directory + '"/*.gcda -f'
    os.system(cmd)
    for i in range(1,100):
        try:
            expected_data = []
            output_file_name = settings['positive_test_output_mask'].replace('*', '{:02d}'.format(i))
            input_file_name = settings['positive_test_input_mask'].replace('*', '{:02d}'.format(i))
            expected_output_file = open(directory + '/' + settings['tests_folder'] + '/' + output_file_name)
            for line in expected_output_file:
                if settings['strict_string']:
                    expected_data.append(line.replace('\n',''))
                else:
                    if line != '':
                        expected_data.append(leave_numbers(line))
            arguments = settings['arguments'].replace('$IN_FILE$', '"' + directory + '/' + settings['tests_folder'] + '/' + input_file_name + '"').replace('$OUT_FILE$', 'tmp.txt')
            cmd = '"' + directory + '/' + settings['app_name'] + '" ' + arguments + ' '
            if settings['use_input_file']:
                cmd += ' < "' + directory + '/' + settings['tests_folder'] + '/' + input_file_name + '"'
            if settings['use_output_file']:
                cmd += '> tmp.txt'
            os.system(cmd)
            recieved_data = []
            recieved_data_file = open(directory + '/tmp.txt')

            reading_result = False
            for line in recieved_data_file:
                if settings['strict_string']:
                    if line.find(settings['result_word']) != -1:
                        reading_result = True
                        line = line[line.find(settings['result_word']):]
                    if reading_result:
                        recieved_data.append(line.replace('\n',''))
                else:
                    if leave_numbers(line) != '':
                        recieved_data.append(leave_numbers(line))

            if recieved_data != expected_data:
                if tests_passed:
                    print(colored('Positive testing unsuccessful', 'red'))
                    tests_passed = False
                print('Test ' + input_file_name + ' has failed:')
                lines = max(len(recieved_data), len(expected_data))
                for i in range(lines - len(recieved_data)):
                    recieved_data.append('')
                for i in range(lines - len(expected_data)):
                    expected_data.append('')
                maximum_length = 0
                for line in expected_data:
                    maximum_length = max(maximum_length, len(line))
                for line in recieved_data:
                    maximum_length = max(maximum_length, len(line))
                maximum_length += 1
                maximum_length = max(16, maximum_length)
                print("  {:Ns} | {:Ns}".replace('N', str(maximum_length)).format("Expected result", "Recieved_result"))
                for i in range(lines):
                    if expected_data[i] != recieved_data[i]:
                        print("* {:Ns} | {:Ns}".replace('N', str(maximum_length)).format(expected_data[i], recieved_data[i]))
                    else:
                        print("  {:Ns} | {:Ns}".replace('N', str(maximum_length)).format(expected_data[i], recieved_data[i]))
        except FileNotFoundError:
            break
    if tests_passed:
        print(colored('Positive testing successful', 'green'))
    print()
    tests_passed = True
    for i in range(1,100):
        try:
            input_file_name = settings['negative_test_input_mask'].replace('*', '{:02d}'.format(i))
            open(directory + '/' + settings['tests_folder'] + '/' + input_file_name)
            arguments = settings['arguments'].replace('$IN_FILE$', directory + '/' + settings['tests_folder'] + '/' + input_file_name).replace('$OUT_FILE$', 'tmp.txt')
            cmd = '"' + directory + '/' + settings['app_name'] + '" ' + arguments + ' '
            if settings['use_input_file']:
                cmd += '" < "' + directory + '/' + settings['tests_folder'] + '/' + input_file_name + '"'
            if settings['use_output_file']:
                cmd += '> tmp.txt'
            if os.WEXITSTATUS(os.system(cmd)) == 0:
                if tests_passed:
                    print(colored('Negative testing unsuccessful', 'red'))
                tests_passed = False
                print('Test ' + input_file_name + ' has failed')
        except FileNotFoundError:
            break
    
    if tests_passed:
        print(colored('Negative testing successful', 'green'))
    if settings['coverage']:
        print(colored('Coverage:', 'blue'))
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(".gcno"):
                    cmd = 'gcov "' + directory + '/' + file + '"'
                    os.system(cmd)
    os.chdir(prev_directory)