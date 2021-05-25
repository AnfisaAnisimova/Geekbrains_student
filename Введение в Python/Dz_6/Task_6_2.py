with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    data_gen = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    data_dict = {}
    for item in data_gen:
        if item[0] not in data_dict:
            data_dict.setdefault(item[0], [item[2]])
        else:
            data_dict[item[0]].append(item[2])

max_val_len = 1
for key, value in data_dict.items():
    if len(value) > max_val_len:
        max_val_len = len(value)
        result = key
print(f'IP-адрес спамера: {result}. Количество отправленных запросов: {max_val_len}.')





