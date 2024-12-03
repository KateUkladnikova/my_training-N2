# "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = list(zip(first, second))

first_result=(len(zp[i][0])-len(zp[i][1]) for i in range(0,len(zp)) if len(zp[i][0])!=len(zp[i][1]))
second_result=(len(first[i])<=len(second[i]) for i in range(0,len(first)))

print(list(first_result))
print(list(second_result))