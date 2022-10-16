# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
# Из семинара 4 дз 3
# 20 20 21 5 6 7 6 123 66 78 123 5 => 21, 7, 66, 78

lst = list(map(int, input('Введите числа через пробел: ').split()))

num_dict = {}
for elem in lst:
    num_dict[elem] = num_dict.get(elem, 0) + 1

uniq_list = [key for key, value in num_dict.items() if value == 1]

print(f'Не повторяющиеся значения: {uniq_list}')
