from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

info_gen = (item for item in zip_longest(tutors, classes, fillvalue=None))

print(type(info_gen), *info_gen)
