# Задача "Нули ничто, отрицание недопустимо!":
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for i in range(0,len(my_list)):
    if my_list[i] < 0:
        break
    while my_list[i] > 0:
        print(my_list[i])
        break