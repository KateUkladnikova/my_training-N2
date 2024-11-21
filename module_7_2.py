# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.
# Написать усовершенствованную функцию записи.
# Задача "Записать и запомнить":
import io
from pprint import pprint

strings = []
def custom_write(file_name, strings):
    # file_name - file for writting
    # strings = strings list for writting
    n_bait_nachalo = []
    for j in range(0, len(strings)):
        n_bait_nachalo.append(0)
    file = open(file_name, 'x')
    file.close()
    file = open(file_name, 'r+', encoding='utf-8')
    for i in range(0,len(strings)):
        n_bait_nachalo[i] = file.tell()
        file.write(f'{strings[i]}\n')
    file.close()
    strings_positions = {}
    for i in range(0, len(strings)):
        strings_positions[(i+1,n_bait_nachalo[i])] = strings[i]
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


