# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
#  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input('Введите числа списка через запятую: ').replace(' ', '').split(',')))

def dif_frac_part(lst):
    frac_part = lst[0] - int(lst[0])
    min_frac = frac_part
    max_frac = frac_part
    for elem in lst:
        frac_part = elem - int(elem)
        if frac_part != 0:
            if frac_part > max_frac:
                max_frac = frac_part
            elif frac_part < min_frac:
                min_frac = frac_part
    return round(max_frac - min_frac, 2)

print(f'{lst} => {dif_frac_part(lst)}')