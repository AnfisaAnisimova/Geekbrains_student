import os
import shutil

dirs_structure = {'my_project':
    [
        {'settings': ['__init__.py', 'dev.py', 'prod.py']},
        {'mainapp': ['__init__.py', 'models.py', 'views.py', {'templates': {'mainapp': ['base.html', 'index.html']}}]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': {'authapp': ['base.html', 'index.html']}}]}
    ]
}

for key, value in dirs_structure.items():
    if not os.path.exists(key):
        for item in value:
            for k, v in item.items():
                os.makedirs(os.path.join(key, k))
                for i in v:
                    if type(i) == str:
                        new_file = open(os.path.join(key, k, i), 'w')
                    elif type(i) == dict:
                        for k_1, v_1 in i.items():
                            os.makedirs(os.path.join(key, k, k_1))
                            if type(v_1) == dict:
                                for k_2, v_2 in v_1.items():
                                    os.makedirs(os.path.join(key, k, k_1, k_2))
                                    if type(v_2) == list:
                                        for f in v_2:
                                            new_file = open(os.path.join(key, k, k_1, k_2, f), 'w')


os.chdir(key)
root_dir = os.getcwd()
for root, dirs, files in os.walk(root_dir):
    if root.endswith('templates'):
        shutil.copytree(root, (os.path.join(root_dir, 'templates')), dirs_exist_ok=True)



