# Задача "Изменять нельзя получать"
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __new__(cls, *args):
        return object.__new__(cls)
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power
    def get_model(self):
        model = f"Модель: {self.__model}"
        return model
    def get_horsepower(self):
        horsepower = f"Мощность двигателя: {self.__engine_power}"
        return horsepower
    def get_color(self):
        return str(f"Цвет: {self.__color}")
    def print_info(self):
        g1 = vehicle1.get_model()
        print(g1)
        g2 = vehicle1.get_horsepower()
        print(g2)
        g3 = vehicle1.get_color()
        print(g3)
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем, что поменялось
vehicle1.print_info()