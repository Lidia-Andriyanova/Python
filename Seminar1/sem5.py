# Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

num = int(input('Введите число: '))

def div_num(number):
    return (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and not number % 30 == 0

if div_num(num):
    print('кратно')
else:
    print('не кратно')

