from termcolor import colored

def open_settings(default_settings = [], directory=''):
    try:
        settings_file = open(directory + 'config.ft', 'r')
        settings = default_settings
        for line in settings_file:
            setting = line.split(': ')[0]
            if setting in settings:
                file_value = line[len(setting) + 1:]
                value = None
                if file_value.count('"') >= 2:
                    value = file_value[file_value.find('"') + 1: file_value.rfind('"')]
                else:
                    try:
                        value = int(file_value)
                    except:
                        if file_value.strip().lower() == 'true':
                            value = True
                        if file_value.strip().lower() == 'false':
                            value = False
                if type(default_settings[setting]) != type(value):
                    print(colored('Parameter "', 'red') +  '{:s}'.format(setting) + colored('" can\'t be assinged "', 'red') + '{:s}'.format(file_value.strip('\n')) +  colored('".','red'))
                    print(colored('Using default value', 'blue'))
                else:
                    settings[setting] = value
            else:
                print(colored('No such parameter "', 'red') + setting + colored('"', 'red'))
        settings_file.close()
        return settings
    except OSError:
        settings_file = open(directory + 'config.ft', 'w')
        for setting in default_settings:
            if type(default_settings[setting]) == str:
                line = setting + ': "' + default_settings[setting] + '"\n'
            else:
                line = setting + ': ' + str(default_settings[setting]) + '\n'
            settings_file.write(line)
        settings_file.close()
        return default_settings
