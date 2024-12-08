#  Тема "Декораторы" в Python
# Цель задания: Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор
# и обернув ею другую функцию.

from math import floor, sqrt

def is_prime(sum_three):
    def wrapper(a, b, c):
        k = 0
        m = sum_three(a, b, c)
        f = False
        for i in range(2, floor(sqrt(m))+1):
            if m % i == 0:
                f = True
                break
        if not f:
            print("Простое")
        else:
            print("Составное")
        return m
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

