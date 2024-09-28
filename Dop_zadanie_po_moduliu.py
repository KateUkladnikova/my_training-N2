grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# вычислим средние баллы учеников и составим список average_grades, содержащий средние баллы:
average_grades = []
for i in grades: average_grades.append(sum(i)/len(i))
# print(average_grades)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# print(students)

# переведем множество students в список students_spisok:
students_spisok = list(students)
# print(students_spisok)

# отсортируем students_spisok в алфавитном порядке:
res = students_spisok. sort()
# print(students_spisok)

# составим словарь my_dict, ключами которого будут элементы отсортированного в алфавитном порядке
# списка students_spisok, а значениями - средние баллы учеников из списка average_grades:
my_dict = {}
for i in range(0,len(students_spisok)): my_dict[students_spisok[i]]=average_grades[i]
print(my_dict)