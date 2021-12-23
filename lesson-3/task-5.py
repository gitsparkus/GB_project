"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
  get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random


def get_jokes(n=1, reuse=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    stuff_list = [nouns, adverbs, adjectives]
    random.shuffle(stuff_list)

    jokes_list = []
    if n > len(nouns) and not reuse:
        print(f'Шуток будет чуть поменьше, потому что {n} > {len(nouns)}')
        n = len(nouns)
    for i in range(n):
        joke_str = ''
        for lst in stuff_list:
            r = random.randrange(len(lst))
            joke_str += (' ' if joke_str else '') + (lst[r] if reuse else lst.pop(r))
        jokes_list.append(joke_str)
    return jokes_list

print(get_jokes(reuse=False))
print(get_jokes(4, reuse=False))
print(get_jokes(9, reuse=False))
