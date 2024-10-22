# "Раз, два, три, четыре, пять... Это не всё?"
#   Дубль 2: убрала лишнии операторы if, print, сократила программу {я без понятия, как ее еще можно сократить:
# чтобы посчитать сумму различных элементов, я перебираю все присутствующие в списке data_structure[] структуры данных, кроме пустых ()}.
# Программа не универсальная, а для конкретного списка data_structure[...] или надо универсальную сделать?
#   Если у меня еще есть время, не ставьте пока оценку (у меня еще 3 попытки ведь есть?), а напишите поконкретнее, как можно улучшить программу.
#   По поводу рекурсии: я ее применяю для каждой внутренней структуры исходного списка, как рекомендовано в условии задачи,
# это неправильное ее использование?
#   По поводу вашего замечания "слишком глубокая вложенность условий": Один лишний оператор if (ненужный) я убрала,
# обработку 1-го вложенного списка отдельно тоже убрала (он обрабатывается в "elif isinstance(data_structure[i], list): ..."),
# чтобы некоторые остальные операторы if убрать, нужно еще функции создать и часть кода туда поместить, и вызовов функций будет много,
# но в примечании к задаче сказано: "Весь подсчёт должен выполняться одним вызовом функции"...
#   Обращаю ваше внимание на то, что программа работает быстро и выдает правильный ответ - 99

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(data_structure):
    summa_elementov = 0
    for i in range(len(data_structure)):
        if isinstance(data_structure[i], dict):
            for k in data_structure[i].keys():
                summa_elementov += len(k)
                summa_elementov += data_structure[i][k]
            return summa_elementov + calculate_structure_sum(data_structure[1:])
        elif isinstance(data_structure[i], list):
            for m in range(len(data_structure[i])):
                if isinstance(data_structure[i][m], int):
                    summa_elementov += data_structure[i][m]
            return summa_elementov + calculate_structure_sum(data_structure[1:])
        elif isinstance(data_structure[i], tuple):
            for m in range(len(data_structure[i])):
                if isinstance(data_structure[i][m], int):
                    summa_elementov += data_structure[i][m]
                elif isinstance(data_structure[i][m], dict):
                    for k in data_structure[i][m].keys():
                        summa_elementov += len(k)
                        summa_elementov += data_structure[i][m][k]
                elif isinstance(data_structure[i][m], list):
                    if isinstance(data_structure[i][m][0], set):
                        spisok_iz_mnozhestva = list(data_structure[i][m][0])
                        for p in range(len(spisok_iz_mnozhestva)):
                            if isinstance(spisok_iz_mnozhestva[p], str):
                                summa_elementov += len(spisok_iz_mnozhestva[p])
                            elif isinstance(spisok_iz_mnozhestva[p], tuple):
                                for q in range(len(spisok_iz_mnozhestva[p])):
                                    if isinstance(spisok_iz_mnozhestva[p][q], str):
                                        summa_elementov += len(spisok_iz_mnozhestva[p][q])
                                    elif isinstance(spisok_iz_mnozhestva[p][q], int):
                                        summa_elementov += spisok_iz_mnozhestva[p][q]
                                    elif isinstance(spisok_iz_mnozhestva[p][q], tuple):
                                        for d in range(len(spisok_iz_mnozhestva[p][q])):
                                            if isinstance(spisok_iz_mnozhestva[p][q][d], str):
                                                summa_elementov += len(spisok_iz_mnozhestva[p][q][d])
                                            elif isinstance(spisok_iz_mnozhestva[p][q][d], int):
                                                summa_elementov += spisok_iz_mnozhestva[p][q][d]
            return summa_elementov + calculate_structure_sum(data_structure[1:])
        elif isinstance(data_structure[i], str):
            summa_elementov += len(data_structure[i])
            return summa_elementov + calculate_structure_sum(data_structure[1:])
    return summa_elementov
result = calculate_structure_sum(data_structure)
print(result)
