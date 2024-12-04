#  "Создание функций на лету"
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
# Задача "Функциональное разнообразие":
# Lambda-функция:

from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
x = first[0]
y = second[0]
rez = list(map(lambda x, y: x == y, first, second))
print(rez)

# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        # print("The file does not exist.")
        file = open(file_name, 'x', encoding='utf-8')
        file = open(file_name, 'a', encoding='utf-8')
        for data_se in data_set:
            file.write(f'{data_se}\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self, *words):
        return choice(self.words)
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())




