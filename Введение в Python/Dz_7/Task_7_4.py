import os
from collections import defaultdict
import django

root_dir = django.__path__[0]
django_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        max_size = 10
        file_size = os.stat(os.path.join(root, file)).st_size
        while file_size >= max_size:
            max_size *= 10
        django_files[max_size] += 1

for key, value in sorted(django_files.items()):
    print(f'{key}: {value}')

