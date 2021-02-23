some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
index = 0
for element in some_list:

    if element.isdigit():
        new_element = '"' + f'{int(some_list[index]):02d}' + '"'
        new_list.append(new_element)
        index += 1
    elif element.startswith("+") or element.startswith("-"):
        new_element = '"' + element[0] + f'{int(some_list[index][1:]):02d}' + '"'
        new_list.append(new_element)
        index += 1
    else:
        new_list.append(element)
        index += 1

print(new_list)

message = ' '.join(new_list)
print(message)
