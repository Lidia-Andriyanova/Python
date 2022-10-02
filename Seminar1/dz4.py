# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

def quarter_area(num):
    if num == 1:
        return '1 четверть -> x > 0 и y > 0'
    elif num == 2:
        return '2 четверть -> x < 0 и y > 0'
    elif num == 3:
        return '3 четверть -> x < 0 и y < 0'
    elif num == 4:
        return '4 четверть -> x > 0 и y < 0'
    else:
        return 'такой четверти нет'

print(quarter_area(quarter))
