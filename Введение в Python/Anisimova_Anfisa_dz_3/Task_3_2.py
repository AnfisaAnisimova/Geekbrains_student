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


def num_translate_adv(eng_number):
    if eng_number.lower() in numbers_dict and eng_number.istitle():
        eng_number = eng_number.lower()
        print(numbers_dict[eng_number].capitalize())
    elif eng_number in numbers_dict:
        print(numbers_dict[eng_number])
    elif eng_number.lower() in numbers_dict and eng_number.isupper():
        eng_number = eng_number.lower()
        print(numbers_dict[eng_number].upper())
    else:
        print(None)


num_translate_adv('One')
num_translate_adv('two')
num_translate_adv('three')
num_translate_adv('FOUR')
num_translate_adv('five')
num_translate_adv('six')
num_translate_adv('seven')
num_translate_adv('eight')
num_translate_adv('nine')
num_translate_adv('ten')
num_translate_adv('fifteen')
