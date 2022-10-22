import model
import view


def work_with_db():
    db, db_cursor = model.db_init()

    while True:
        view.print_main_menu()
        main_menu_item = view.choose_main_menu()
        if main_menu_item == '1':
            result_list = model.select_all_data(db_cursor)
            view.print_list(result_list)
        elif main_menu_item == '2':
            new_employee_lst = view.new_employee()
            message = model.insert_data(db, db_cursor, new_employee_lst)
            view.print_message(message)
        elif main_menu_item == '3':
            delete_id = view.input_id()
            message = model.delete_data(db, db_cursor, delete_id)
            view.print_message(message)
        elif main_menu_item == '4':
            edit_option = view.choose_edit_option()
            if edit_option in [1, 2, 3]:
                edit_id = view.input_id()
                field_name = view.edit_field_name(edit_option)
                field_value = view.edit_field_value(edit_option)
                message = model.edit_data(db, db_cursor, field_name, field_value, edit_option in [2, 3], edit_id)
                view.print_message(message)
            else:
                print('Некорректный выбор')
        elif main_menu_item == '5':
            last_name = view.input_data('фамилию сотрудника')
            result_list = model.find_data(db_cursor, last_name)
            view.print_list(result_list)
        elif main_menu_item == '6':
            result_list = model.stat_data(db_cursor)
            view.print_stat_data(result_list)
        elif main_menu_item.lower() in ['q', 'й']:
            print('Программа работы с сотрудниками завершена')
            break
        else:
            print('Повторите ввод действия')
        view.back_main_menu()
