def test_function():
    def inner_function():
        x = 'Я в области видимости функции test_function'
        print(x)
    result_inner_function = inner_function()

# result_inner_function = inner_function() --> если вызываем вне функции test_function, то на консоли появляется ошибка:
# "NameError: name 'inner_function' is not defined." (дословно "имя 'inner_function' не определено"),
# т. к. функция inner_function находится в области видимости функции test_function и не определена за ее пределами.

result = test_function()

