def phone_book_write(file_name, phone_dict):
    with open(file_name, 'w', encoding='utf-8') as file_info:
        for k, v in phone_dict.items():
            file_info.write(v[0] + '\n')
            file_info.write(v[1]+ '\n')
            file_info.write(k + '\n')
            file_info.write('\n')

def phone_book_read(file_name, phone_dict):
    with open(file_name, 'r', encoding='utf-8') as file_info:
        count = 1
        last_name = ''
        first_name = ''
        for line in file_info:
            line = line.replace('\n', '').replace('\ufeff', '')
            if count % 4 == 1:
                last_name = line
            elif count % 4 == 2:
                first_name = line
            elif count % 4 == 3:
                phone_dict[line] = (last_name, first_name)
            count += 1

def add_phone(phone_dict, record):
    phone, last_name, first_name = record
    if phone not in phone_dict:
        phone_dict[phone] = (last_name, first_name)
        return True, f'Добавлен {last_name} {first_name} с телефоном {phone}'
    else:
        return False, f'Такой телефон {phone} уже есть в справочнике у {phone_dict[phone][0]} {phone_dict[phone][1]}'

def edit_phone(phone_dict, record):
    phone, last_name, first_name = record
    find_list = list(filter(lambda key: phone_dict[key] == (last_name, first_name), phone_dict.keys()))
    if len(find_list) != 0:
        del phone_dict[find_list[0]]
        phone_dict[phone] = (last_name, first_name)
        return True, f'Телефон у {last_name} {first_name} изменен на {phone}'
    else:
        return False, f'Записи с такой фамилией {last_name} и именем {first_name} нет в справочнике'

def del_phone(phone_dict, record):
    phone, last_name, first_name = record
    find_list = list(filter(lambda key: phone_dict[key] == (last_name, first_name), phone_dict.keys()))
    if len(find_list) != 0:
        del phone_dict[find_list[0]]
        return True, f'Запись {last_name} {first_name} удалена'
    else:
        return False, f'Записи с такой фамилией {last_name} и именем {first_name} нет в справочнике'

def find_phone(phone_dict, record):
    phone, last_name, first_name = record
    find_list = list(filter(lambda key: phone_dict[key] == (last_name, first_name), phone_dict.keys()))
    if len(find_list) != 0:
        return True, f'У {last_name} {first_name} телефон: {find_list[0]}'
    else:
        return False, f'Записи с такой фамилией {last_name} и именем {first_name} нет в справочнике'

