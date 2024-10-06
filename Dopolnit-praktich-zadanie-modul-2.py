# Дополнительное практическое задание по модулю: "Основные операторы"/ задание "Слишком древний шифр"
import random
n = int(input ('введите число от 3 до 20 для первого поля: '))
# print(n)
chislo_diapazona = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Para = ''
result = ''
for i in range(0,n):
    for j in range(1,n):
        if chislo_diapazona[i] != chislo_diapazona[j] and n % (chislo_diapazona[i] + chislo_diapazona[j]) == 0:
            if chislo_diapazona[i] > chislo_diapazona[j]:
                continue
            Para = str(chislo_diapazona[i]) + str(chislo_diapazona[j])
            result = result + Para
print(result)





