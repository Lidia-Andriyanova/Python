# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число: '))

def binary_num(num):
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res

print(f'{num} -> {binary_num(num)}')