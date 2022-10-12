# Напишите программу, удаляющую из текста все слова, содержащие 'абв'
# 'абв роро длдлдл оооабв лоло абв' => 'роро длдлдл лоло'

txt = input('Введите текст: ')
sb_str = input('Введите подстроку: ')

def del_word(txt, sub_str):
    lst = txt.split()
    i = len(lst) - 1
    while i >= 0:
        if lst[i].find(sub_str) != -1:
            lst.pop(i)
        i -= 1
    res = ''
    for elem in lst:
        if res != '':
            res += ' '
        res += elem
    return res

print(del_word(txt, sb_str))

