# "Потоки на классах"
# "За честь и отвагу!"

import time
from time import sleep
import threading
from tkinter.font import names
from turtledemo.penrose import start

# Создание класса
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
    def run(self):
        print(f'{self.name}, на нас напали!')
        voini = 100
        for den in range(1,11):
            voini -= self.power
            print(f'{self.name} сражается {den} день(дня)..., осталось {voini} воинов.')
            time.sleep(1)
            if voini==0:
                break
        print(f'{self.name} одержал победу спустя {den} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')




