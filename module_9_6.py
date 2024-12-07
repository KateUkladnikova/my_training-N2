# темa "Генераторы"
# Цель: более глубоко понять особенности
# работы с функциями генераторами и оператором yield в Python.

def all_variants(text):
    j = 0
    while j != len(text):
        if j == 0:
            for l in range(len(text)):
                yield text[j+l]
        else:
            for k in range(j-1, j):
                yield text[j-1] + text[j]
        j += 1
    yield text
a = all_variants("abc")
for i in a:
    print(i)
