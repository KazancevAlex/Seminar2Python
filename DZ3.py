# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('Введите количество чисел в списке '))

def numbers(n):
    summa = 0
    for i in range(n):
        a = int(input(f'Введи число {i + 1} '))
        a = (1+1/a)**a
        summa = a + summa
        i += 1
    return summa

print('Сумма чисел = ',round((numbers(n)), 2))