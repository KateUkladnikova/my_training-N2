# "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2]
not_primes = []
is_prime = 'False'
delitel = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(0,len(numbers)):
    for j in range(0,numbers[i]):
        if numbers[i] > delitel[j]:
            if numbers[i] % delitel[j] != 0:
                k = i
                is_prime = 'True'
            else:
                is_prime = 'False'
                not_primes.append(numbers[i])
                break
    if is_prime == 'True':
        primes.append(numbers[k])
print('Primes: ', primes)
print('Not Primes: ', not_primes)