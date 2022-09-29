# Вывести на экран числа от -N до N

num = int(input('Введите число: '))

def print_num(number):
    number = abs(number)
    first = number*(-1)
    second = number
    while first <= second:
        print(f'{first}', end = ' ')
        first += 1

print_num(num)
