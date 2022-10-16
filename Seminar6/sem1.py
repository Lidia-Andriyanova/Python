# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# 1 - 2 * 3 => -5
# (1 + 2) * 3 => 9

exp = input('Введите выражение: ')

lst = list(exp)

digit_str = ''.join(list(filter(lambda x: x not in [' ', '+', '-', '*', '/', '(', ')'], lst)))

if digit_str.isdigit():
    code = compile(exp, "<string>", "eval")
    print(exp, '=', eval(code))
else:
   print('Введено не числовое выражение')
