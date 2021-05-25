from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(quantity, flag=False):
    """возращает n количество шуток из заданных списков"""
    index = quantity
    if flag:
        while index != 0 and len(nouns) != 0:
            joke = f'"{nouns.pop(randrange(len(nouns)))}' \
                   f' {adverbs.pop(randrange(len(adverbs)))}' \
                   f' {adjectives.pop(randrange(len(adjectives)))}" '
            print(joke)
            index -= 1
    else:
        while index != 0:
            joke = f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"'
            print(joke)
            index -= 1


get_jokes(6, True)

