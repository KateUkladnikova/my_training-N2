immutable_var = (1, [4,5], 'String', True)
print(immutable_var)
# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа:
#
# immutable_var[0] = 2 - ошибка: "TypeError: 'tuple' object does not support item assignment", т.к.
# переменной immutable_var присвоен кортеж (тип tuple) - неизменяемый тип данных.
mutable_list = [5, False, 4.9]
mutable_list[0] = 9
mutable_list[1] = 'String'
mutable_list[2] = 100
print(mutable_list)