# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time

def pseudo_random(min_num, max_num):
    if min_num > max_num:
        min_num, max_num = max_num, min_num

    curr_time = str(time.time())
    num = int(curr_time[-3:])
    if num == 0:
        num = 1000

    dif = max_num - min_num + 1
    res = int(min_num + dif * num / 1000)
    return res


min_num = int(input('Введите минимум: '))
max_num = int(input('Введите максимум: '))
print(f'Случайное число из диапазона: {pseudo_random(min_num, max_num)}')




