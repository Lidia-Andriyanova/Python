# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: '))

def neg_fib(num):
    lst = []
    if num >= 1:
        lst.append(1)
    if num >= 2:
        lst.append(-1)
    for i in range(2, num):
        lst.append(lst[i -2] - lst[i - 1])
    res = []
    for elem in lst:
        res.insert(0, elem)
    return res

def pos_fib(num):
    lst = []
    if num >= 1:
        lst.append(1)
    if num >= 2:
        lst.append(1)
    for i in range(2, num):
        lst.append(lst[i -2] + lst[i - 1])
    return lst

def fib(num):
    neg_lst = neg_fib(num)
    zero_lst = [0]
    pos_lst = pos_fib(num)
    return neg_lst + zero_lst + pos_lst

if num >= 0:
    print(fib(num))
else:
    print('Введите положительное число')



