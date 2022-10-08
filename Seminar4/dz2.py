# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

num = int(input('Введите натуральное число: '))

def simple_div(num):
    lst = []
    div = 2
    while div <= num:
        if num % div == 0:
            lst.append(div)
            num /= div
            div = 1
        div += 1
    return lst

print(simple_div(num))

