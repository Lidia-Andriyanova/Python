from random import randint
from time import sleep
from pprint import pprint

lst = ['3', '5', '6', '4', '9']
res = map(int, lst)


# print(res)
# res2 = map(lambda x: x + 2, res)
# print(tuple(res2))

def more_five(x):
    if x > 5:
        return True


res = filter(more_five, res)
print(list(res))

new = [2, 5, 8, 9, 6]
res_map = map(more_five, new)
print(list(res_map))

list_cmp = [randint(0, 10) for i in range(10) if i % 2 == 0]
print(list_cmp)

set_cmp = {randint(0, 10) for i in range(10) if i % 2 == 0}
print(set_cmp)

dict_cmp = {i: randint(0, 10) for i in range(10)}
print(dict_cmp)

dict_cmp = {str(i): randint(0, 10) for i in range(10)}
print(dict_cmp)

dict_cmp = {(i, i + 1): randint(0, 10) for i in range(10)}
print(dict_cmp)

x = 5
print(id(x))
x = 4
print(id(x))
y = 4
print(id(y))

x = '5'
print(id(x))
x = '4'
print(id(x))
y = '4'
print(id(y))

x = [1, 2, 3]
print(id(x))
x.append(17)
print(id(x))

# генератор
gen = (randint(0, 10) for i in range(10) if i % 2 == 0)
print(gen)
print(gen.__next__())
print(gen.__next__())
print(list(gen))
print(list(gen))  # второй раз пустой

print('-------------')


def mult(x):
    # sleep(1)
    return x * 2


rand_list = [mult(i) for i in range(5)]
# print(rand_list)
gen_list = (mult(i) for i in range(5))

for i in rand_list:
    print(i)

for i in gen_list:
    print(i)

print('-------------')

for w in enumerate(rand_list):
    print(w)

print('-------------')

eval('print(55)')

my_dict = {
    'age': 28,
    'city': 'Yesk',
    'last_name': 'Sergeev',
    'name': 'Sacha',
    'status': 'married'
}

pprint(my_dict)
print('Возвраст: ', my_dict.get('age', 54))
print('Есть машина: ', my_dict.get('is_car', True))
my_dict.setdefault('is_car', False)
pprint(my_dict)

second_dict = {
    'age': 22,
    'city': 'Tomsk',
    'height': 185,
    'last_name': 'Derbeev',
    'name': 'Pacha',
}

print('-------------')

my_dict.update(second_dict)
pprint(my_dict)

print('-------------')

for k, v in my_dict.items():
    print(k, v)