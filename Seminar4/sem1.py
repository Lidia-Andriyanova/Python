# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

lst = list(map(int, input('Введите строку чисел, для разделителя используя пробел: ').split()))

def max_min(lst):
    max_num = lst[0]
    min_num = lst[0]
    for elem in lst:
        if elem > max_num:
            max_num = elem
        elif elem < min_num:
            min_num = elem
    return max_num, min_num

interval = max_min(lst)
print(f'Максимальное число: {interval[0]}. Минимальное число: {interval[1]}.')

