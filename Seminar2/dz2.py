# Написать программу, получающую набор произведений чисел от 1 до N
# Пример: пусть N = 4, тогда [1, 2, 6, 24]

num = int(input('Введите число: '))

def multiply_list(num):
    list = []
    list.append(1)
    for i in range(1, num):
        list.append(list[i-1] * (i + 1));
    return list

print(f'N = {num} -> {multiply_list(num)}')

