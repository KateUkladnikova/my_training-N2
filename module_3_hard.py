# "Раз, два, три, четыре, пять .... Это не всё?" (Игла Кощея:)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(data_structure):
    summa_elementov = 0
    for i in range(len(data_structure)):
        if i<len(data_structure):
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
                                if isinstance(spisok_iz_mnozhestva[p], int):
                                    summa_elementov += spisok_iz_mnozhestva[p]
                                    print(summa_elementov)
                                elif isinstance(spisok_iz_mnozhestva[p], str):
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
        elif i == 0:
            for m in range(len(data_structure[0])):
                if isinstance(data_structure[0][m], int):
                    summa_elementov += data_structure[0][m]
            return summa_elementov
    return summa_elementov
result = calculate_structure_sum(data_structure)
print(result)
