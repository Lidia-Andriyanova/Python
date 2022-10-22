def print_main_menu():
    print(' ___________________________________')
    print('|        Сотрудники компании:       |')
    print('|___________________________________|')
    print('| 1 - Все                           |')
    print('| 2 - Принять на работу             |')
    print('| 3 - Уволить                       |')
    print('| 4 - Изменить должность/ЗП/бонусы  |')
    print('| 5 - Найти                         |')
    print('| 6 - Статистика                    |')
    print('| q - Выйти                         |')
    print('|___________________________________|')

def choose_main_menu():
    return input(f'Введите действие: ')

def back_main_menu():
    return input(f'Нажмите ввод для возврата в главное меню: ')

def print_list(lst):
    if len(lst) > 0:
        print('Идентификатор'.ljust(15), 'Фамилия'.ljust(15), 'Имя'.ljust(10), 'Должность'.ljust(15), 'Зарплата'.rjust(8), 'Бонус'.rjust(7))
        for elem in lst:
            print(str(elem[0]).center(15), elem[1].ljust(15), elem[2].ljust(10), elem[3].ljust(15), str(elem[4]).rjust(8), str(elem[5]).rjust(7))
    else:
        print('Нет данных')

def new_employee():
    lst = []
    lst.append(input_data('фамилию'))
    lst.append(input_data('имя'))
    lst.append(input_data('должность'))
    lst.append(int(input_data('зарплату')))
    lst.append(int(input_data('бонус')))
    return lst

def input_id():
    return int(input_data('идентификатор сотрудника'))

def choose_edit_option():
    return int(input(f'Выберите изменение: 1 - должность, 2 - зарплата, 3 - бонус: '))

def edit_field_value(edit_option):
    if edit_option == 1:
        return input_data('должность')
    elif edit_option == 2:
        return int(input_data('зарплата'))
    elif edit_option == 3:
        return int(input_data('бонус'))

def edit_field_name(edit_option):
    if edit_option == 1:
        return 'position'
    elif edit_option == 2:
        return 'salary'
    elif edit_option == 3:
        return 'bonus'

def print_stat_data(lst):
    stat_data = lst[0]
    print(f'Максимальная зарплата = {str(stat_data[0]).rjust(8)}')
    print(f'Минимальная зарплата  = {str(stat_data[1]).rjust(8)}')
    print(f'Средняя зарплата      = {str(int(stat_data[2])).rjust(8)}')
    print(f'Максимальный бонус    = {str(stat_data[3]).rjust(8)}')
    print(f'Минимальный бонус     = {str(stat_data[4]).rjust(8)}')
    print(f'Средний бонус         = {str(int(stat_data[5])).rjust(8)}')

def input_data(data_name):
    return input(f'Введите {data_name}: ')

def print_message(message):
    print(message)
    print('')


