# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Из семинара 1 дз 2

from pprint import pprint

def check_pred(x, y, z):
    return not (x or y or z) == (not x and not y and not z)

dict = {(x, y, z): check_pred(x, y, z) for x in range (2) for y in range(2) for z in range(2)}

pprint(dict)


