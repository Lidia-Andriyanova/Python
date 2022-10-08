# Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.

def nod(a, b):
    #print(a, b)
    if b == 0:
        return a
    else:
        return nod(b, a % b)

def nok(a, b):
    return int(abs(a * b) / nod(a, b))

x = 60
y = 40
print(nod(x, y))
print(nok(x, y))