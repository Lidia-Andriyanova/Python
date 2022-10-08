# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141        10^-1 <= d <= 10^-10

import math

precision = float(input('Введите точность от 10^-10 до 10^-1: '))

def round_pi(precision):
    if 10 ** (-10) <= precision <= 10 ** (-1):
        digit_count = 0
        while precision < 1:
            precision *= 10
            digit_count += 1
        if precision > 1:
            print('Точность должна содержать только нули и единицы в дробной части')
        else:
            print(f'Число π с точностью до {digit_count} знаков после запятой: {round(math.pi, digit_count)}')
    else:
        print('Введена точность не из указанного интервала')

round_pi(precision)

