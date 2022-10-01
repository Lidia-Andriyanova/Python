# Для натурального n сздать список, состоящий из элементов последовательности 3n + 1
# Пример:
# Для n = 6: [4, 7, 10, 13, 16, 19]

num = int(input('Введите число: '))

def sequence_list(num):
    list = []
    for i in range(1, num + 1):
        element = 3 * i + 1
        list.append(element)
    return list

list = sequence_list(num)
print(list)