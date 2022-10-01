# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в списке position - создайте этот список
# (например positions = [1, 3, 6]

num = int(input('Введите число: '))

str = input('Введите список позиций, разделяя их запятыми: ')
str = str.replace(' ', '')
positions = list(map(int, str.split(',')))

def fill_list(num):
    list = []
    for i in range(-num, num + 1):
        list.append(i)
    return list

list = fill_list(num)

def multiplay_positions(list, positions):
    result = 1
    for pos in positions:
        if 0 <= pos <= len(list) - 1:
            result *= list[pos]
    return result

print(f'Список: {list}')
print(f'Позиции: {positions}')
print(f'Произведение элементов на позициях: {multiplay_positions(list, positions)}')

