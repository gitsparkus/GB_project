import os

CONFIG = 'config.yaml'
ROOT = './'

temp_list = []

with open(CONFIG, 'r', encoding='UTF-8') as config_f:
    for line in config_f:
        indent = line.count('   ') - 1
        temp_list[indent:] = [line.strip()]
        fullpath = os.path.join(ROOT, *temp_list)
        if fullpath.endswith(':'):
            fullpath = fullpath.replace(':', '')
            if not os.path.exists(fullpath):
                os.makedirs(fullpath)
        else:
            fullpath = fullpath.replace(':', '')
            with open(fullpath, 'w', encoding='UTF-8') as new_f:
                pass
