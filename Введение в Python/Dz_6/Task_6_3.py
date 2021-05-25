import json
from itertools import zip_longest
import sys


with open("users.csv", "r", encoding="utf-8") as users:
    users_list = users.read().replace(',', ' ').split("\n")

with open("hobby.csv", "r", encoding="utf-8") as hobbies:
    hobbies_list = hobbies.read().split("\n")

if len(users_list) >= len(hobbies_list):
    info_dict = dict(zip_longest(users_list, hobbies_list, fillvalue=None))
else:
    sys.exit(1)
print(info_dict)

info_str = json.dumps(info_dict, ensure_ascii=False, indent=4)

with open("info.json", "w", encoding="utf-8") as info:
    info.write(info_str)