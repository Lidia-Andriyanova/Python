import sqlite3

def db_init():
    db = sqlite3.connect('company.db')
    db_cursor = db.cursor()
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
           id INTEGER PRIMARY KEY,
           last_name TEXT,
           first_name TEXT,
           position TEXT,
           salary INTEGER,
           bonus INTEGER)
        ''')
    db.commit()
    db_cursor.execute('SELECT * FROM persons')
    one_result = db_cursor.fetchone()
    if one_result == None:
        person_lst = [
        (1, 'Сидоров', 'Валерий', 'Директор', 90000, 50000),
        (2, 'Иванов', 'Иван', 'Главный инженер', 50000, 10000),
        (3, 'Александрова', 'Ольга', 'Секретарь', 20000, 1000),
        (4, 'Сидорчук', 'Виктор', 'Мастер', 30000, 1000),
        (5, 'Сидоренко', 'Виталий', 'Механик', 20000, 1000)
        ]
        db_cursor.executemany('INSERT INTO persons VALUES(?,?,?,?,?,?)', person_lst)
        db.commit()
    return db, db_cursor

def select_all_data(db_cursor):
    db_cursor.execute('SELECT * FROM persons')
    all_result = db_cursor.fetchall()
    return all_result

def insert_data(db, db_cursor, new_employee_lst):
    max_id = get_max_id(db_cursor)
    new_employee_lst.insert(0, max_id + 1)
    person_list = [tuple(new_employee_lst)]
    try:
        db_cursor.executemany('INSERT INTO persons VALUES(?,?,?,?,?,?)', person_list)
        db.commit()
        return 'Новый сотрудник принят на работу'
    except:
        'Нового сотрудника не удалось принять на работу'

def get_max_id(db_cursor):
    db_cursor.execute('SELECT MAX(id) AS max_id FROM persons')
    one_result = db_cursor.fetchone()
    return one_result[0]

def delete_data(db, db_cursor, id):
    db_cursor.execute(f'DELETE FROM persons WHERE id = {id}')
    db.commit()
    return f'Сотрудник с идентификатором {id} уволен'

def edit_data(db, db_cursor, field_name, field_value, is_int_type, id):
    sql_query = f'UPDATE persons SET {field_name} = ? WHERE id = ?'
    if is_int_type:
        field_value = int(field_value)
    data = (field_value, id)
    db_cursor.execute(sql_query, data)
    db.commit()
    return f'Сотрудник с идентификатором {id} изменен'

def find_data(db_cursor, name):
    sql_query = f'SELECT * FROM persons WHERE last_name LIKE ?'
    data = (f'%{name}%',)
    db_cursor.execute(sql_query, data)
    all_result = db_cursor.fetchall()
    return all_result


def stat_data(db_cursor):
    db_cursor.execute('''SELECT
        MAX(salary),
        MIN(salary),
        AVG(salary),
        MAX(bonus),
        MIN(bonus),
        AVG(bonus)        
        FROM persons''')
    all_result = db_cursor.fetchall()
    return all_result

