# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input('Введите числа через пробел: ').split()))

def uniq_list(lst):
    num_dict = dict()
    for elem in lst:
        if elem not in num_dict:
            num_dict[elem] = 1
        else:
            num_dict[elem] += 1
    res_list = []
    for i in num_dict:
        if num_dict[i] == 1:
            res_list.append(i)
    return res_list

print(f'Не повторяющиеся значения: {uniq_list(lst)}')
