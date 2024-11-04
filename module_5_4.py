# "Различие атрибутов класса и экземпляра"
# Задача "История строительства"
class House:
# В классе House создаем атрибут houses_history = []
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
    pass
h1 = House('ЖК Эльбрус', number_of_floors = 10)
print(House.houses_history)
h2 = House('ЖК Акация', number_of_floors = 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', number_of_floors = 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)