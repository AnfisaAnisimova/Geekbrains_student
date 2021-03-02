declension_list = ["процент", "процента", "процентов"]

for number in range(1, 20):

    if number == 1:
        print(number, declension_list[0])
    elif 1 < number < 5:
        print(number, declension_list[1])
    else:
        print(number, declension_list[2])
