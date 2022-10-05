# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#П ример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input('Введите числа списка через запятую: ').replace(' ', '').split(',')))

def pair_multiply(lst):
    len_lst = len(lst)
    pair_count = len_lst // 2
    if len_lst % 2 == 1:
        pair_count += 1
    res = []
    for i in range(pair_count):
        res.append(lst[i] * lst[len_lst - 1 - i])
    return res

print(f'{lst} => {pair_multiply(lst)}')
