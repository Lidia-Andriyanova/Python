# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

lst = input('Введите значения списка через пробел: ').split()
num = input('Введите число: ')

if num in lst:
    print(f'Число {num} присутствует в списке {lst}')
else:
    print(f'Число {num} отсутствует в списке {lst}')




