# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import expressions

k1 = int(input('Введите степень первого многочлена: '))
k2 = int(input('Введите степень второго многочлена: '))

file_name1 = 'polynom_1.txt'
file_name2 = 'polynom_2.txt'
min_coef = -100
max_coef = 100

expressions.file_write(file_name1, expressions.polynom(expressions.coefficients(k1, min_coef, max_coef)))
expressions.file_write(file_name2, expressions.polynom(expressions.coefficients(k2, min_coef, max_coef)))

poly1 = expressions.file_read(file_name1)
poly2 = expressions.file_read(file_name2)

print(poly1)
coefs1 = expressions.coefs_from_polynom(poly1)

print(poly2)
coefs2 = expressions.coefs_from_polynom(poly2)

coef_sum = expressions.polynom_sum(coefs1, coefs2)
poly_sum = expressions.polynom(coef_sum)
print('Сумма многочленов:')
print(poly_sum)



