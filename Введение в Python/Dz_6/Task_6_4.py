import sys

with open("users.csv", "r", encoding="utf-8") as users:
    users_list = users.read().replace(',', ' ').split("\n")

with open("hobby.csv", "r", encoding="utf-8") as hobbies:
    hobbies_list = hobbies.read().split("\n")

if len(users_list) >= len(hobbies_list):
    with open("users_hobby.txt", "a", encoding="utf-8") as ush:
        ush.writelines(f'{users_list[i]}: {hobbies_list[i]}\n' for i in range(len(users_list)))
else:
    sys.exit(1)

# пыталась переделать, не понимаю, почему не работает
import sys
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobbies:
        if len(users.readlines()) >= len(hobbies.readlines()):
            users_hobbies = zip_longest(users, hobbies, fillvalue=None)
            for item in users_hobbies:
                with open("users_hobby.txt", "a", encoding="utf-8") as ush:
                    ush.write(f'{item[0].strip()}: {item[1].strip()}\n')
        else:
            sys.exit(1)