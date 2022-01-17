import os

CONFIG = 'config.yaml'
ROOT = './'

path_list = []

with open(CONFIG, 'r', encoding='UTF-8') as config_f:
    for line in config_f:
        if not line.startswith('#'):
            indent = line.count('   ') - 1
            path_list[indent:] = [line.strip()]
            fullpath = os.path.join(ROOT, *path_list)
            if fullpath.endswith(':'):
                fullpath = fullpath.replace(':', '')
                try:
                    os.makedirs(fullpath)
                except FileExistsError as e:
                    print(f'Каталог {fullpath} уже существует.')
            else:
                fullpath = fullpath.replace(':', '')
                with open(fullpath, 'w', encoding='UTF-8') as new_f:
                    pass
