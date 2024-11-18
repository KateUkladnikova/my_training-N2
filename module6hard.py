# Дополнительное практическое задание по модулю: "Наследование классов."
# Задание "Они все так похожи"

from math import pi, sqrt
class Figure():
    sides_count = 0
    def __init__(self, __color, *__sides, filled = None):
        self.__color = __color
        self.__sides = __sides
        self.filled = filled
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        color_korr = False
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r>=0 and g>=0 and b>=0 and r<=256 and g<=256 and b<=256:
                color_korr = True
                return color_korr
    def set_color(self, r, g, b):
        if Figure.__is_valid_color(self,r, g, b):
            self.__color = [r, g, b]
        else:
            self.__color = list(self.__color)
    def __is_valid_sides(self, sides):
        side_korr = False
        side_good = 0
        if len(sides) == len(self.__sides):
            for i in range(0, len(sides)):
                if isinstance(sides[i], int) and sides[i]>0:
                    side_good += 1
        if side_good == len(sides):
            side_korr = True
        return side_korr
    def get_sides(self):
        return self.__sides
    def __len__(self):
        perimetr = sum(self.__sides)
        return perimetr
    def set_sides(self, *new_sides):
        new_side = []
        for j in range(0, 100):
            if list(new_sides)[j] != None:
                new_side.append(new_sides[j])
                break
        if len(new_side) == self.sides_count:
            self.__sides = new_side
        elif (self.sides_count == 3):
            for i in range(0,2):
                self.__sides[i] = 1
        return self.__sides
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides, radius=1):
        super().__init__(color, sides)
        self.radius = float(list(sides)[0]) / (2 * pi)
    def get_square(self):
        return pi * self.radius ** 2
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides)
    def get_square(self):
        p = sum(self.get_sides()) / 2
        s = sqrt(p * (p - float(list(self.get_sides())[0])) * (p - float(list(self.get_sides())[1])) * (p - float(list(self.get_sides())[2])))
        return s
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.sides = sides
    def get_sides(self):
        if len(self.sides) == 1:
            tmp_sides = list(self.sides)
            for i in range(0, 11):
                tmp_sides.append(list(self.sides)[0])
        return tmp_sides
    def get_volume(self):
        self.get_sides()
        return int(self.get_sides()[0]) ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())








