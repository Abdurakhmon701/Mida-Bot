import sqlite3
from openpyxl import Workbook

def db_to_xlsx(db_name, table_name):
    # Подключаемся к базе данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Извлекаем данные из таблицы
    cursor.execute(f"SELECT * FROM users")
    data = cursor.fetchall()

    # Создаем новый файл Excel и лист
    wb = Workbook()
    ws = wb.active

    # Записываем заголовки столбцов
    columns = [i[0] for i in cursor.description]
    ws.append(columns)

    # Записываем данные
    for row in data:
        ws.append(row)

    # Сохраняем файл
    wb.save('users.xlsx')
    return wb








