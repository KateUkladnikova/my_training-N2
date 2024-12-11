# "Потоковая запись в файлы"
# Импорты необходимых модулей и функций

import time
from time import sleep
import threading

# Объявление функции write_words
def wite_words(word_count, file_name):
    # Взятие текущего времени
    started_at = time.time()
    # Запуск функций с аргументами из задачи
    file = open(file_name, 'x', encoding='utf-8')
    file.close()
    file = open(file_name, 'r+', encoding='utf-8')
    for i in range(1,word_count+1):
        # print(f'Какое-то слово № {i}\n')
        file.write(f'Какое-то слово № {i}\n')
        time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    file.close()
    # Взятие текущего времени
    ended_at = time.time()
    # Вывод разницы начала и конца работы функций
    elapsed = round(ended_at - started_at, 6)
    return elapsed
m1 = wite_words(10, file_name = 'example1.txt')
m2 = wite_words(30, file_name = 'example2.txt')
m3 = wite_words(200, file_name = 'example3.txt')
m4 = wite_words(100, file_name = 'example4.txt')
print(f'Работа потоков {m1+m2+m3+m4}')
# Взятие текущего времени
started_at = time.time()
# Создание и запуск потоков с аргументами из задачи
thread = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread.start()
thread1 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread1.start()
# m5 = wite_words(30, 'example6.txt')
thread2 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread2.start()
# m6 = wite_words(100, 'example8.txt')
thread3 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
thread3.start()

thread.join()
thread1.join()
thread2.join()
thread3.join()

ended_at = time.time()
# Вывод разницы начала и конца работы функций
elapsed = round(ended_at - started_at, 6)
print(f'Работа потоков {elapsed}')




