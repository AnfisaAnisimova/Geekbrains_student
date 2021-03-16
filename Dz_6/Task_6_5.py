import sys

file_name, users, hobbies, users_hobbies = sys.argv

with open(users, "r", encoding="utf-8") as users:
    users_list = users.read().replace(',', ' ').split("\n")

with open(hobbies, "r", encoding="utf-8") as hobbies:
    hobbies_list = hobbies.read().split("\n")

if len(users_list) >= len(hobbies_list):
    with open(users_hobbies, "a", encoding="utf-8") as ush:
        ush.writelines(f'{users_list[i]}: {hobbies_list[i]}\n' for i in range(len(users_list)))
else:
    sys.exit(1)
