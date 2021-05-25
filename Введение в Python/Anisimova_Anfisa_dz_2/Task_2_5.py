
price_list = [57.8, 46.51, 97, 12.45, 99.09, 72, 68, 23.48, 60, 09.50]
print(id(price_list))

price_list2 = []

price_list.sort()
print(price_list)
print(id(price_list))

for number in price_list:
    if type(number) == int:
        price_list2.append(f'{number} руб 00 коп')
    else:
        number = f'{number:.2f}'
        index = number.find(".")
        rub, kop = number[:index], number[index + 1:]
        price_list2.append(f'{rub} руб {int(kop):02d} коп')

prices = ''.join(str(price_list2))
print(prices)
print(type(prices))

price_list_descending = list(reversed(price_list2))
print(price_list_descending)

the_most_exp_goods = price_list2[-5:]
print(the_most_exp_goods)




