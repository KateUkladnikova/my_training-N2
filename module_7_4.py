# Различные методы форматирования строк в Python.
# Применить эти методы в контексте описания соревнования. История: соперничество двух команд -
# Мастера кода и Волшебники данных.
# Использование %

team1_num = 5
print('В команде Мастера кода участников: %s' % team1_num,'!')
team2_num = 6
print( 'Итого сегодня в командах участников: %s' % team1_num, 'и %s' % team2_num, '!')
score_1 = 40
score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(42),'!')
team1_time = 1552.512
print('Волшебники данных решили задачи за {}'.format(team1_time), '!')
print(f'Команды решили {score_1} и {score_2} задач.')
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = print(f'Результат битвы: победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = print(f'{challenge_result}')
else:
    result = print(f'Ничья!')
