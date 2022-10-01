# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

num = int(input('Введите число: '))

def sequence_list(num):
    list = []
    sum = 0
    for i in range(1, num + 1):
        element = round((1 + 1/i)**i, 3)
        list.append(element)
        sum += element
    return (list, sum)

(list, sum) = sequence_list(num)

print(list)
print(sum)

