# Создайте программу для игры с конфетами человек против человека

import random

sweet_count = 100
take_count = 28

def do_step(player_type, step_count, cur_player, sweet_count, take_count, can_take):
    if player_type == 1: # Игрок
        return int(input(f'Ход {step_count}. Игрок {cur_player}. Количество конфет: {sweet_count}. Можно взять: {can_take}: '))
    elif player_type == 2: # Бот
        auto_take = random.randint(1, can_take)
        print(f'Ход {step_count}. Игрок {cur_player}. Количество конфет: {sweet_count}. Можно взять: {can_take}. Взято: {auto_take}')
        return auto_take
    else: # Бот с интеллектом
        if can_take == sweet_count:
            auto_take = can_take
        elif sweet_count % (take_count + 1) != 0:
            auto_take = sweet_count % (take_count + 1)
        else:
            auto_take = 1
        print(f'Ход {step_count}. Игрок {cur_player}. Количество конфет: {sweet_count}. Можно взять: {can_take}. Взято: {auto_take}')
        return auto_take

def Game(game_type, sweet_count, take_count, first_player, second_player, who_first):
    first_player_step = True
    step_count = 1
    while sweet_count > 0:
        can_take = take_count if take_count < sweet_count else sweet_count
        cur_player = first_player if first_player_step else second_player

        if game_type == 1 or who_first == 1 and first_player_step or who_first == 2 and not first_player_step:
            player_type = 1 # Игрок
        elif game_type == 2:
            player_type = 2 # Бот
        else:
            player_type = 3 # Бот с интеллектом

        take = do_step(player_type, step_count, cur_player, sweet_count, take_count, can_take)
        if take > can_take or take <= 0:
            print(f'Можно взять только: {can_take}')
            continue
        sweet_count -= take
        step_count += 1
        first_player_step = not first_player_step
    return cur_player


game_type = int(input('Выберите тип игры: 1 - два игрока, 2 - игра с ботом, 3 - игра с ителлектуальным ботом: '))
if 1 <= game_type <= 3:
    if game_type == 1:
        first_player = input('Введите имя первого игрока: ')
        second_player = input('Введите имя второго игрока: ')
        print(f'Выиграл игрок {Game(game_type, sweet_count, take_count, first_player, second_player, 0)}!')
    else:
        who_first = int(input('Кто будет ходиться первым 1 - Игрок, 2 - Бот: '))
        if who_first == 1:
            first_player = input('Введите имя игрока: ')
            second_player = 'Бот' if game_type == 2 else 'Бот с интеллектом'
        elif who_first == 2:
            first_player = 'Бот' if game_type == 2 else 'Бот с интеллектом'
            second_player = input('Введите имя игрока: ')
        else:
            print('Неправильно выбрана очередность ходов')
            exit()
        print(f'Выиграл игрок {Game(game_type, sweet_count, take_count, first_player, second_player, who_first)}!')
else:
    print('Неправильно выбран тип игры')


