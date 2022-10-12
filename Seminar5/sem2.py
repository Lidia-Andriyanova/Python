lst = [3, 5, 6, 4, 9]
print(lst)
def summ(x):
    return x + 2

# res = list(map(float, lst))
# res = list(map(summ, lst))
# res = list(map(lambda x: x * 2, lst))
# print(res)

def more_five(x):
    if x > 5:
        return True

res = list(filter(more_five, lst))
print(res)