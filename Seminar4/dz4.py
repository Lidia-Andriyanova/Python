# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import expressions

k = int(input('Введите степень многочлена: '))

if k >= 0:
    coefs = expressions.coefficients(k, 0, 100)
    poly = expressions.polynom(coefs)
    file_name = 'polynom.txt'
    expressions.file_write(file_name, poly)
    print(poly)
    print(f'Записано в {file_name}')
else:
    print('Степень многочлена должна быть не меньше нуля')




