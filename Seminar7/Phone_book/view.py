def print_main_menu():
    print(' ____________________________')
    print('|  Телефонный справочник:    |')
    print('|____________________________|')
    print('| 1 - Просмотр               |')
    print('| 2 - Добавить               |')
    print('| 3 - Изменить               |')
    print('| 4 - Удалить                |')
    print('| 5 - Найти                  |')
    print('| 6 - Сохранить              |')
    print('| 7 - Экспортировать         |')
    print('| 8 - Выйти                  |')
    print(' ----------------------------')

def choose_main_menu():
    return int(input(f'Введите действие: '))

def back_main_menu():
    return input(f'Нажмите ввод для возврата в главное меню: ')

def print_message(message):
    print(message)
    print('')

def view_phone_book(phone_dict):
    print('')
    print('Список номеров:')
    for item in phone_dict.items():
        print(item[0], item[1][0] + ' ' + item[1][1])
    print('')

def input_record(menu_item):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = ''
    if menu_item == 2:
        phone = input('Введите телефон: ')
    elif menu_item == 3:
        phone = input('Введите новый телефон: ')
    return phone, last_name, first_name

def choose_export_format():
    return int(input(f'Введите формат экспорта 1 - json, 2 - csv: '))

