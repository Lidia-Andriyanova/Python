# Реализовать алгоритм перемешивания списка

list = input('Введите список элементов, разделя их пробелами: ').split()

def mix_list(list):
    for i in range(1, len(list), 2):
        temp = list[i]
        list[i] = list[i-1]
        list[i-1] = temp
    temp = list[0]
    list[0] = list[len(list)-1]
    list[len(list)-1] = temp
    return list

print(f'Исходный список: {list}')
print(f'Перемешанный список: {mix_list(list)}')
