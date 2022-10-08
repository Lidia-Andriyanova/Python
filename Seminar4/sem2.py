# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# с помощью математических формул нахождения корней квадратного уравнения

a = int(input('Введите коэффициент А: '))
b = int(input('Введите коэффициент B: '))
c = int(input('Введите коэффициент C: '))

lst = (a, b, c)

def discriminant(lst):
    a, b, c = lst
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / 2 * a
        return x1, None
    elif d > 0:
        x1 = (-b + d ** 0.5)/ (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
    else:
        return None, None

print(discriminant(lst))