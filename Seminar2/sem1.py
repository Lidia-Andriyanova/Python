# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

num = int(input('Введите число: '))

def print_sequence(num):
    res = 1;
    print(res, end='')
    for i in range(num - 1):
        res *= -3
        print(f', {res}', end='')

print_sequence(num)
