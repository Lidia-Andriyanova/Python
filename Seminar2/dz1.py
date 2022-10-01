# Подсчитать сумму цифр в вещественном числе

num = input('Введите вещественное число: ')

def float_sum(num):
    num = num.replace('.', '')
    result = 0
    for digit in num:
        result += int(digit)
    return result

print(f'Сумма цифр {float_sum(num)}')


