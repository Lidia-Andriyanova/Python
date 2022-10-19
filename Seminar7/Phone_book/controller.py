import model
import view
import exporter

def record_operation(phone_dict, main_menu_item):
    record = view.input_record(main_menu_item)
    if main_menu_item == 2:
        result = model.add_phone(phone_dict, record)
    elif main_menu_item == 3:
        result = model.edit_phone(phone_dict, record)
    elif main_menu_item == 4:
        result = model.del_phone(phone_dict, record)
    elif main_menu_item == 5:
        result = model.find_phone(phone_dict, record)
    view.print_message(result[1])

def work_with_phone_book():
    file_name = 'phone_book'
    file_ext_txt = '.txt'
    file_ext_json = '.json'
    file_ext_csv = '.csv'
    phone_dict = dict()
    model.phone_book_read(file_name + file_ext_txt, phone_dict)

    while True:
        view.print_main_menu()
        main_menu_item = view.choose_main_menu()
        if main_menu_item == 1:
            view.view_phone_book(phone_dict)
        elif main_menu_item in range(2, 6):
            record_operation(phone_dict, main_menu_item)
        elif main_menu_item == 6:
            model.phone_book_write(file_name + file_ext_txt, phone_dict)
            view.print_message(f'Телефонный справочник записан в {file_name + file_ext_txt}')
        elif main_menu_item == 7:
            export_format = view.choose_export_format()
            if export_format == 1:
                exporter.export_json(file_name + file_ext_json, phone_dict)
                view.print_message(f'Телефонный справочник записан в {file_name + file_ext_json}')
            elif export_format == 2:
                exporter.export_csv(file_name + file_ext_csv , phone_dict)
                view.print_message(f'Телефонный справочник записан в {file_name + file_ext_csv}')
        elif main_menu_item == 8:
            exit()
        else:
            print('Повторите ввод действия')
        view.back_main_menu()


