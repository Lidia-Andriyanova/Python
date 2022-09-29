# Найти максимально из пяти чисел

def MaxValue(list):
    max = list[0]
    for x in list:
        if x > max:
           max = x
    return max

list = [4, 34, 78, 9, 12]
print(MaxValue(list))
