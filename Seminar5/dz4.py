# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def file_read(file_name):
    with open(file_name, 'r') as file_info:
        return file_info.readlines()

def file_write(file_name, in_list):
    with open(file_name, 'w') as file_info:
        file_info.writelines(in_list)

def puck(in_list):
    new_list = []
    for ln in in_list:
        ln = ln.replace('\n', '')
        sym = ''
        res_str = ''
        count = 0
        for elem in ln:
            if elem != sym:
                if sym != '':
                    res_str = res_str + str(count + 1) + sym
                    count = 0
            else:
                count += 1
            sym = elem
        res_str = res_str + str(count + 1) + sym
        if ln != in_list[len(in_list) - 1]:
            res_str = res_str + '\n'
        new_list.append(res_str)
    return new_list

def unpuck(in_list):
    new_list = []
    for ln in in_list:
        ln = ln.replace('\n', '')
        res_str = ''
        num_str = ''
        for elem in ln:
            if elem.isdigit():
                num_str = num_str + elem
            else:
                res_str = res_str + elem * int(num_str)
                num_str = ''

        if ln != in_list[len(in_list) - 1]:
            res_str = res_str + '\n'
        new_list.append(res_str)
    return new_list

start_file = 'start.txt'
start_list = file_read(start_file)
print(f'Исходные строки из файла {start_file}: {start_list}')

puck_file = 'puck.txt'
puck_list = puck(start_list)
file_write(puck_file, puck_list)
print(f'Сжатые строки записаны в файл {puck_file}: {puck_list}')
print()

puck2_list = file_read(puck_file)
print(f'Сжатые строки из файла {puck_file}: {puck2_list}')

unpuck_file = 'unpuck.txt'
unpuck_list = unpuck(puck2_list)
file_write(unpuck_file, unpuck_list)
print(f'Восстановленные строки записаны в файл {unpuck_file}: {unpuck_list}')

