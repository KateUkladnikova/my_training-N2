#  "Учёт товаров"
import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        str1 = f"{self.name}, {self.weight}, {self.category}"
        return str1

class Shop:
    def __init__(self):
        self.name = ""
        self.weight = 0.0
        self.category = ""
        self.__file_name = 'products.txt'
    def get_products(self):
        current_directory = os.getcwd()
        # print("The current working directory is:", current_directory)
        # Проверяю, существует ли этот файл
        if os.path.exists(current_directory+"/products.txt"):
            # print("The file exists.")
            file = open(self.__file_name, 'r+')
            stroka = file.read()
            file.close()
        else:
            # print("The file does not exist.")
            file = open(self.__file_name, 'x')
            file.close()
            file = open(self.__file_name, 'r')
            stroka = ''
            file.close()
        return stroka
    def add(self, *products):
        for i in products:
            if self.get_products().find(f'{i.name}, {i.weight}, {i.category}') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i.__str__()}\n')
                file.close()
            else:
                print(f'Продукт {i.name}, {i.weight}, {i.category} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1,p2,p3)
print(s1.get_products())

