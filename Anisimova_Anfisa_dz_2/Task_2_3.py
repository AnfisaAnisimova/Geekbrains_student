some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
for element in some_list:

    if element.isdigit():
        new_element = '"' + f'{int(some_list[index]):02d}' + '"'
        some_list[index] = new_element
        index += 1

    elif element.startswith("+") or element.startswith("-"):
        new_element = '"' + element[0] + f'{int(some_list[index][1:]):02d}' + '"'
        some_list[index] = new_element
        index += 1

    else:
        index += 1
        continue

print(some_list)

message = ' '.join(some_list)
print(message)