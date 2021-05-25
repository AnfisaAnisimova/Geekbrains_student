numbers_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(eng_number):

    if eng_number in numbers_dict:
        result = numbers_dict[eng_number]
        print(result)
    else:
        print(None)


num_translate('one')
num_translate('two')
num_translate('three')
num_translate('four')
num_translate('five')
num_translate('six')
num_translate('seven')
num_translate('eight')
num_translate('nine')
num_translate('ten')
num_translate('fifteen')

# Вариант 2:
#
# numbers_dict = {
#     'one': 'один',
#     'two': 'два',
#     'three': 'три',
#     'four': 'четыре',
#     'five': 'пять',
#     'six': 'шесть',
#     'seven': 'семь',
#     'eight': 'восемь',
#     'nine': 'девять',
#     'ten': 'десять'
# }
#
#
# def num_translate(eng_number):
#
#     for key, value in numbers_dict.items():
#         if numbers_dict.get(eng_number) is None:
#             print(None)
#             break
#         elif key == eng_number:
#             result = value
#             print(result)
#
#
# num_translate('one')
# num_translate('two')
# num_translate('three')
# num_translate('four')
# num_translate('five')
# num_translate('six')
# num_translate('seven')
# num_translate('eight')
# num_translate('nine')
# num_translate('ten')
# num_translate('fifteen')

