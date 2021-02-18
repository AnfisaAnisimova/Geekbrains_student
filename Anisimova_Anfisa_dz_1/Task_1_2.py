odd_numbers_cube_list = []

for number in range(0, 1000):
    if number % 2 == 1:
        odd_numbers_cube_list.append(number ** 3)

print(odd_numbers_cube_list)

sum_list = 0

for number in odd_numbers_cube_list:

    sum_num = 0
    n = number

    while number != 0:
        sum_num += number % 10
        number //= 10
    if sum_num % 7 == 0:
        sum_list += n

print(sum_list)

new_list = []

for number in odd_numbers_cube_list:
    new_number = number + 17
    new_list.append(new_number)

print(new_list)

sum_list1 = 0

for number in new_list:

    sum_num = 0
    n = number

    while number != 0:
        sum_num += number % 10
        number //= 10
    if sum_num % 7 == 0:
        sum_list1 += n

print(sum_list1)