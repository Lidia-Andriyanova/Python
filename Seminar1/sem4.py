# Показать первую цифру дробной части числа

num = float(input('Введите дробное число: '))

def first_num(number):
    number *= 10
    number = int(number % 10)
    return number

print(first_num(num))


