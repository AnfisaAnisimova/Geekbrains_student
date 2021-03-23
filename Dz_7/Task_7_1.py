import os

dirs_structure = {'my_ project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, value in dirs_structure.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))


# --------------------------------------альтернативное решение----------------------------------------------------------
# dir_name = 'my_project'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
# os.chdir('my_project')
# dirs_list = ['settings', 'mainapp', 'adminapp', 'authapp']
# for item in dirs_list:
#     if not os.path.exists(item):
#         os.mkdir(item)


