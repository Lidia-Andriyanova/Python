# Рандомная строка

import random

string = ''

for i in range(50):
    string += chr(random.randint(1070, 1100))

print(string)