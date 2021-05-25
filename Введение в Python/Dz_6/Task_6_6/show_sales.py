import sys

with open("bakery.csv", "r", encoding="utf-8") as f:
    if len(sys.argv) == 3:
        data = sys.argv[1]
        data_2 = sys.argv[2]
        data_slice = f.readlines()[int(data)-1:int(data_2)]
        for item in data_slice:
            print(item, end='')
    elif len(sys.argv) == 2:
        data = sys.argv[1]
        data_slice = f.readlines()[int(data) - 1:]
        for item in data_slice:
            print(item, end='')
    else:
        print(f.read())






