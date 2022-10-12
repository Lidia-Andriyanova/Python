# Создайте программу для игры в "Крестики-нолики"

field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def print_field(field):
    print('   ', end= '')
    for row in range(0, len(field)):
        print(str(row + 1), end='  ')
    print()

    for row in range(0, len(field)):
        print(str(row + 1), end='  ')
        for col in range(0, len(field[row])):
            print(field[row][col], end='  ')
        print()

def check_stripe(sign_set):
    if len(sign_set) == 1:
        if '_' not in sign_set:
            return 1 if 'X' in sign_set else 2
    return 0

def check_field(field):
    # Проверка в строках
    for row in range(0, len(field)):
        sign_set = set()
        for col in range(0, len(field[row])):
            sign_set.add(field[row][col])
        player_num = check_stripe(sign_set)
        if player_num != 0:
            return player_num
    # Проверка в столбцах
    for col in range(0, len(field[row])):
        sign_set = set()
        for row in range(0, len(field)):
            sign_set.add(field[row][col])
        player_num = check_stripe(sign_set)
        if player_num != 0:
            return player_num
    # Проверка по первой диагонали
    sign_set = set()
    for row in range(0, len(field)):
        sign_set.add(field[row][row])
    player_num = check_stripe(sign_set)
    if player_num != 0:
        return player_num
    # Проверка по второй диагонали
    sign_set = set()
    for row in range(0, len(field)):
        sign_set.add(field[row][len(field) - 1 - row])
    player_num = check_stripe(sign_set)
    if player_num != 0:
        return player_num
    return 0

def game(field):
    print_field(field)
    first_player = True
    step = 0
    while step < len(field)*len(field[0]):
        coord = list(map(int, input(f'Ход {step + 1}. Игрок {1 if first_player else 2} введите номер строки и колонки через пробел: ').split()))
        if coord[0] in [1, 2, 3] and coord[1] in [1, 2, 3]:
            if field[coord[0] - 1][coord[1] - 1] == '_':
                sign = 'X' if first_player else '0'
                field[coord[0] - 1][coord[1] - 1] = sign

                print_field(field)
                player_num = check_field(field)
                if player_num != 0:
                    print(f'Выиграл игрок {player_num}')
                    exit()

                step += 1
                first_player = not first_player
            else:
                print('Позиция по этим строке и колонке не пустая')
        else:
            print('Неверные номера строки и колонки')

game(field)