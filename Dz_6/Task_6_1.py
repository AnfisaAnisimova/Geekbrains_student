with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    data_list = []
    for line in f:
        info = line.split()
        data_list.append((info[0], info[5][1:], info[6]))

    print(data_list)

# -------------------------------------------альтернативное решение-----------------------------------------------------

with open("nginx_logs.txt", encoding="utf-8") as f:
    data_gen = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)

    print(*data_gen)

