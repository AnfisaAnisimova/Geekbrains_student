
employees_list = ['инженер-конструктор Игорь',
                  'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
index = 0
for info in employees_list:
    name = info.split(" ")
    print("Привет, ", name[-1].capitalize(), "!", sep="")
    index += 1



