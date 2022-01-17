import os
import json

ROOT = './files'

dict_result = dict()
for (dir_path, dir_names, file_names) in os.walk(ROOT):
    for file_name in file_names:
        key_size = '1' + len(str(os.stat(os.path.join(dir_path, file_name)).st_size)) * '0'
        fame, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lstrip('.')
        if key_size in dict_result:
            dict_result[key_size][0] += 1
            dict_result[key_size][1].add(file_extension)
        else:
            dict_result[key_size] = [1, {file_extension}]

dict_result = {k: (v[0], list(v[1])) for k, v in sorted(dict_result.items())}

print(dict_result)

with open(f'{ROOT.rstrip("./")}_summary.json', 'w', encoding='UTF-8') as json_file:
    json.dump(dict_result, json_file, indent=4)
