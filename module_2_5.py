# "Функции в Python.Функция с параметром"
# n - количество строк матрицы matrix, m - количество столбцов матрицы matrix, value - одинаковые
# числовые значения, которыми заполнена матрица matrix.
def get_matrix (n, m, value):
    matrix =[]
    for i in range(0,n):
        l = []
        matrix.append(l)
        for j in range(0, m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)